from flask import Flask, request
import socket
import requests

app = Flask(__name__)

def scan_ports(ip):
    common_ports = [21, 22, 23, 80, 443]
    open_ports = []

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

def get_ip_info(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url).json()
        return {
            "country": response.get("country"),
            "city": response.get("city"),
            "isp": response.get("isp")
        }
    except:
        return None

@app.route('/')
def home():
    return '''
    <h1 style="color:red;">CyberScan Elite 😈🔥</h1>
    <form action="/scan">
        <input type="text" name="target" placeholder="Enter Domain or IP">
        <button type="submit">Scan</button>
    </form>
    '''

@app.route('/scan')
def scan():
    target = request.args.get('target')

    try:
        ip = socket.gethostbyname(target)
        hostname = socket.gethostbyaddr(ip)[0]
        ports = scan_ports(ip)
        info = get_ip_info(ip)

        return f"""
        <h2>Results 😈🔥</h2>
        <p><b>Target:</b> {target}</p>
        <p><b>IP:</b> {ip}</p>
        <p><b>Host:</b> {hostname}</p>
        <p><b>Open Ports:</b> {ports if ports else "None"}</p>

        <h3>🌍 Location Info</h3>
        <p><b>Country:</b> {info['country']}</p>
        <p><b>City:</b> {info['city']}</p>
        <p><b>ISP:</b> {info['isp']}</p>
        """
    except:
        return "<h2>Error ❌ Invalid target</h2>"

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
