# -*- coding: utf-8 -*-
import http.server
import socketserver
import os
import socket

PORT = 8085
for p in [8085, 8080, 8000, 5000, 3000]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('127.0.0.1', p))
        s.close()
        PORT = p
        break
    except Exception:
        pass

web_dir = r"C:\Users\HP TTS\.gemini\antigravity\scratch"
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

with ThreadedHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Server started on http://localhost:{PORT}/")
    httpd.serve_forever()
