from http.server import BaseHTTPRequestHandler, HTTPServer

class BotHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/ping":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Pong from C2!")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(('', 80), BotHandler)
    print("C2 Server running on port 80")
    server.serve_forever()
