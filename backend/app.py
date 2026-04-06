from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_response(404)
            self.end_headers()

    # Вывод нужных логов
    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"🚀 Backend started on port {port}")
    server.serve_forever()