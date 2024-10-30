# Reverse Proxy with Caching, Load Balancing, and Access Control

## Overview

A **reverse proxy** acts as an intermediary server that handles client requests on behalf of backend servers. Unlike a **forward proxy**, which operates on the client side by masking the client’s identity from external servers, a reverse proxy sits on the server side. It represents the backend servers to the client, making it appear as if all requests and responses are directly between the client and the proxy.

### Key Differences

- **Reverse Proxy**:
  - Intercepts client requests and routes them to the appropriate backend server.
  - Improves performance, load balancing, and security for backend services.
  - Seen as part of the backend infrastructure by the client.

- **Forward Proxy**:
  - Sits on the client side to interact with external services on the internet.
  - Commonly used to mask client IP addresses or enforce network policies.
  - Seen as part of the client’s infrastructure by external services.

## Services Offered by a Reverse Proxy

1. **Load Balancing**: 
   - Distributes client requests across multiple backend servers to avoid overloading a single server. Common algorithms include round-robin, least connections, and IP hashing.

2. **Caching**:
   - Stores responses from backend servers to serve repeated requests faster and reduce server load. Cached responses also improve latency for frequently accessed resources.

3. **Access Control**:
   - Filters client requests based on IP addresses, authentication tokens, or other security mechanisms, adding a layer of protection for backend resources.

## Project Setup and Workflow

In this project, the reverse proxy server performs load balancing, caching, and access control over multiple backend servers. Here’s a step-by-step guide to deploying and managing the setup:

### Step 1: Launch the Backend Servers

1. **Run `launch-servers.sh`**: This script builds the Docker image and runs containers for each backend server.
   - The script initializes multiple instances of backend servers on separate ports, preparing them to receive requests from the reverse proxy.

### Step 2: Launch the Proxy Server

2. **Run the Proxy Script `proxy.py`**:
   - Start the proxy by running the main script and add flags for each service (-c to enable caching | -a  configuring access control).
   - The proxy server will begin receiving and processing client requests, routing them to the appropriate backend server based on load balancing rules.

### Step 3: Test the Proxy Server

3. **Run the `test-proxy.py` Script**:
   - This script simulates client requests to the proxy server, testing the functionality of load balancing, caching, and access control.
   - Concurrent requests help verify that the proxy distributes requests evenly and caches responses as intended.

### Step 4: Stop the Servers

4. **Run the `stop-servers.sh` Script**:
   - This script gracefully stops all backend server containers and the proxy server, cleaning up resources and closing connections.

## Conclusion

With this setup, your reverse proxy server effectively manages client requests by distributing load, caching frequently accessed responses, and enforcing access control. This configuration optimizes backend performance and improves scalability and security for client-facing applications.
