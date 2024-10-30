# build image
docker build -t flask-backend .

# run 3 containers  : 

# Run the first instance of the Flask application
docker run -d --name flask-backend1 -p 5001:5000 flask-backend  # Maps host port 5001 to container port 5000

# Run the second instance of the Flask application
docker run -d  --name flask-backend2 -p 5002:5000 flask-backend  # Maps host port 5002 to container port 5000

# Run the third instance of the Flask application
docker run -d  --name flask-backend3 -p 5003:5000 flask-backend  # Maps host port 5003 to container port 5000