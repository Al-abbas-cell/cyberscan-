from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>CyberScan 😈</h1>
    <form action="/scan">
        <input type="text" name="target" placeholder="Enter IP or Domain">
        <button type="submit">Scan</button>
    </form>
    '''

@app.route('/scan')
def scan():
    target = request.args.get('target')

    try:
        ip = socket.gethostbyname(target)
        return f"""
        <h2>Result 😈:</h2>
        <p>Target: {target}</p>
        <p>IP Address: {ip}</p>
        """
    except:
        return "<h2>Error ❌: Invalid target</h2>"

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
