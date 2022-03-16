from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from your swf host \"%s\".\n' % socket.gethostname()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
