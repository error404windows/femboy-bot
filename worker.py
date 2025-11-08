import threading
import time
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_server():
    server = HTTPServer(('0.0.0.0', 8080), Handler)
    print("Keep-alive server running on port 8080...")
    server.serve_forever()

# Start the HTTP server in a separate thread
threading.Thread(target=run_server, daemon=True).start()

# Keep alive logic
while True:
    time.sleep(300)
    print("Ping! Still alive.")
