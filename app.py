from flask import Flask
import os
import socket

app = Flask(__name__)   # ✅ Correct – double underscores

@app.route('/')
def hello():
    version = os.environ.get('VERSION', 'v2.0')
    hostname = socket.gethostname()
    return f"Hello from {hostname} running version {version} (updated!)\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
