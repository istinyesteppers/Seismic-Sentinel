"""
Dashboard Launcher for Seismic Sentinel.
Starts a local server and opens the frontend automatically.
"""
import webbrowser
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Configuration
PORT = 8000
HOST = "localhost"

def run_server():
    """Starts the HTTP server and opens the default browser."""
    server_address = (HOST, PORT)
    
    try:
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    except OSError as e:
        print(f"Error: Port {PORT} is busy. Try closing other python windows.")
        sys.exit(1)

    url = f"http://{HOST}:{PORT}/frontend/index.html"
    
    print("-" * 50)
    print(f"🌍 SEISMIC SENTINEL DASHBOARD IS LIVE")
    print("-" * 50)
    print(f"✅ Server Status:  Online")
    print(f"👉 Dashboard URL:  {url}")
    print("-" * 50)
    print("Press Ctrl+C to stop the server...")

    # Automatically open the web browser
    webbrowser.open(url)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server... Goodbye!")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
