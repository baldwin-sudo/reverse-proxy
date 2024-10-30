import requests

PROXY_URL = 'http://localhost:8080/hello'  # URL of the proxy server

def send_requests(num_requests):
    for i in range(num_requests):
        response = requests.get(PROXY_URL)
        print(f"Request {i + 1}: {response.text}")

if __name__ == "__main__":
    send_requests(20)
