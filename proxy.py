from flask import Flask, request, Response
import requests
import argparse

app = Flask(__name__)

# List of backend servers
BACKEND_SERVERS = [
    'http://localhost:5001',  # First backend server
    'http://localhost:5002',  # Second backend server
    'http://localhost:5003',  # Third backend server
]
SERVER_INDEX = 0  # Initialize the server index at the top level

# Cache for GET requests
ENABLE_CACHE = False
CACHE = {}

# Access control: block users by IP address
ACCESS_CONTROL = False
BLOCKED_IPS = ['192.168.1.4', '192.168.1.3', '192.168.1.2']


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    global SERVER_INDEX, ENABLE_CACHE, ACCESS_CONTROL  # Ensure these are recognized as global variables

    # Access control: check if IP is blocked
    client_ip = request.remote_addr
    if ACCESS_CONTROL and client_ip in BLOCKED_IPS:
        return Response(f"Access denied. Your IP address {client_ip} is blocked.", status=403)

    # Round-robin selection of backend server
    server = BACKEND_SERVERS[SERVER_INDEX]
    SERVER_INDEX = (SERVER_INDEX + 1) % len(BACKEND_SERVERS)  # Increment SERVER_INDEX in a round-robin fashion

    # Check cache for GET requests
    if ENABLE_CACHE:
        if request.method == "GET" and path in CACHE:
            cached_response = CACHE[path]
            print("Serving response from cache...")
            return Response(
                cached_response["content"].decode() + " served from cache...",
                status=cached_response["status"],
                content_type=cached_response["content_type"]
            )

    # Forward the request to the selected backend server
    url = f"{server}/{path}"
    if request.method == 'POST':
        response = requests.post(url, json=request.json)
    elif request.method == 'PUT':
        response = requests.put(url, json=request.json)
    elif request.method == 'DELETE':
        response = requests.delete(url)
    else:
        # GET request
        response = requests.get(url)

    # Cache the response for GET requests
    if ENABLE_CACHE and request.method == "GET":
        CACHE[path] = {
            "content": response.content,
            "status": response.status_code,
            "content_type": response.headers['Content-Type']
        }
        print("Response is cached...")

    # Add a note to the response content to identify the server that handled it
    response_content = response.content.decode() + f" (Response from server on port: {server.split(':')[-1]})"
    return Response(response_content, status=response.status_code, content_type=response.headers['Content-Type'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A simple proxy providing load balancing, caching, and access control services.")
    
    parser.add_argument("-c", "--enable-cache", action="store_true", help="Enable caching service")
    parser.add_argument("-a", "--access-control", action="store_true", help="Enable access control")

    args = parser.parse_args()

    # Set global variables based on parsed arguments
    ENABLE_CACHE = args.enable_cache
    ACCESS_CONTROL = args.access_control

    app.run(port=8080)
