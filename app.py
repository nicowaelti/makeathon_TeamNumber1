from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')  # Render the index.html template

# No need to use app.run() since Azure will handle the server in production
