from flask import Flask, request

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
    return f"<h2>Result 😈:</h2><p>You entered: {target}</p>"

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
