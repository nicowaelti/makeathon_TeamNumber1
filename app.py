from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return send_file('index.html')  # Serve index.html from the root directory

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
