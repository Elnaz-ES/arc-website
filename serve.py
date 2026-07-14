import http.server, socketserver, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control","no-store, max-age=0")
        super().end_headers()
PORT=4173
with socketserver.TCPServer(("",PORT),H) as httpd:
    print(f"serving no-cache on :{PORT}"); httpd.serve_forever()
