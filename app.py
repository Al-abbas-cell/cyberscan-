from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>CyberScan 😈</h1>
    <form action="/scan">
        <input type="text" name="target" placeholder="Enter target">
        <button type="submit">Scan</button>
    </form>
    '''

@app.route('/scan')
def scan():
    target = request.args.get('target')
    if not target:
        return "No target provided"

    result = os.popen(f"ping -c 4 {target}").read()

    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
