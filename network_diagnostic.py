import subprocess
import socket
import requests
import speedtest


def simple_ping(host):
    try:
        result = subprocess.run(["ping", "-n", "4", host], capture_output=True, text=True)
        if "TTL=" in result.stdout:
            return True
        return False
    except Exception:
        return False


def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return "Unavailable"


def get_public_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except Exception:
        return "Unavailable"


def test_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000  # Convert to Mbps
        upload = st.upload() / 1_000_000      # Convert to Mbps
        ping = st.results.ping
        return round(download, 2), round(upload, 2), round(ping, 2)
    except Exception:
        return None, None, None


def main():
    print("🧠 Network Diagnostics - Paulo Henrique Edition\n")

    print("🔌 Checking gateway connection...")
    if simple_ping("192.168.0.1"):
        print("✅ Gateway is reachable.\n")
    else:
        print("❌ Could not reach the gateway.\n")

    print("📡 Checking internet connectivity (Google DNS)...")
    if simple_ping("8.8.8.8"):
        print("✅ Internet is reachable.\n")
    else:
        print("❌ No internet access detected.\n")

    print("🌐 Getting IP addresses...")
    print(f"Local IP: {get_local_ip()}")
    print(f"Public IP: {get_public_ip()}\n")

    print("🚀 Running internet speed test...")
    download, upload, ping = test_speed()
    if download:
        print(f"Download Speed: {download} Mbps")
        print(f"Upload Speed: {upload} Mbps")
        print(f"Ping: {ping} ms")
    else:
        print("❌ Speed test failed.\n")

    print("\n🧠 Diagnostic complete. Have a good day!\n")


if __name__ == "__main__":
    main()
