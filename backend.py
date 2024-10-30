from flask import Flask, jsonify

app = Flask(__name__)

# this is the docker container port  , it can be anything 
PORT =5000
@app.route('/hello')
def hello():
    return jsonify(message=f"Hello from the backend! ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)  # Make sure to bind to all interfaces
