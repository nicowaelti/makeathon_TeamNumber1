from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def hello_world():
    return send_file('index.html')  # Serve index.html from the root directory

# No need to use app.run() since the server will handle this in production
