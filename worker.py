import threading
import time
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

# Simple web server to respond to Render pings
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_server():
    server = HTTPServer(('0.0.0.0', 8080), Handler)
    server.serve_forever()

# Start web server in background
threading.Thread(target=run_server, daemon=True).start()

print("Keep-alive server running on port 8080...")

# Ping itself every 5 minutes to stay awake
while True:
    time.sleep(300)
    print("Ping! Still alive.")
