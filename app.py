from flask import Flask, request
import socket
import requests

app = Flask(__name__)

# فحص بورتات محدودة (للتجربة فقط)
def scan_ports(ip):
    open_ports = []
    ports = [21, 22, 80, 443, 3306, 8080]

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass

    return open_ports


@app.route('/')
def home():
    return """
    <h1>Cyber Scanner 😈</h1>
    <form action="/scan">
        <input name="target" placeholder="Enter IP or Domain">
        <button type="submit">Scan</button>
    </form>
    """


@app.route('/scan')
def scan():
    target = request.args.get('target')

    try:
        ip = socket.gethostbyname(target)
    except:
        return "Invalid target"

    # معلومات الموقع من API
    res = requests.get(f"http://ip-api.com/json/{ip}").json()

    info = {
        "country": res.get("country", "Unknown"),
        "city": res.get("city", "Unknown"),
        "isp": res.get("isp", "Unknown"),
        "lat": res.get("lat", 0),
        "lon": res.get("lon", 0)
    }

    # فحص البورتات
    ports = scan_ports(ip)

    # رابط الخريطة الصحيح
    map_url = f"https://www.google.com/maps?q={info['lat']},{info['lon']}"

    return f"""
    <h2>Results 😈🔥</h2>

    <p><b>Target:</b> {target}</p>
    <p><b>IP:</b> {ip}</p>

    <p><b>Open Ports:</b> {ports if ports else "None"}</p>

    <h3>🌍 Location Info</h3>
    <p><b>Country:</b> {info['country']}</p>
    <p><b>City:</b> {info['city']}</p>
    <p><b>ISP:</b> {info['isp']}</p>

    <a href="{map_url}" target="_blank">📍 View on Map</a>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
