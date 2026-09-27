# -*- coding: utf-8 -*-
import http.server
import socketserver
import os
import socket
import sys

candidate_ports = [8090, 8000, 5500, 8888, 9000, 3000, 5000, 8085]
chosen_port = None

for p in candidate_ports:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('127.0.0.1', p))
            chosen_port = p
            break
    except Exception as e:
        print(f"Port {p} not available: {e}")

if not chosen_port:
    print("Could not find free port")
    sys.exit(1)

os.chdir(r"C:\Users\HP TTS\.gemini\antigravity\scratch")
Handler = http.server.SimpleHTTPRequestHandler

print(f"STARTING_SERVER_PORT_{chosen_port}", flush=True)

with socketserver.TCPServer(("127.0.0.1", chosen_port), Handler) as httpd:
    print(f"HTTP Server running on http://localhost:{chosen_port}/", flush=True)
    print(f"Guide PDF Direct URL: http://localhost:{chosen_port}/pdf_guide_lina_rela.html", flush=True)
    httpd.serve_forever()
