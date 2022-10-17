# ウェブサーバーの立ち上げ
import http.server
import socketserver

with socketserver.TCPServer(
        ('127.0.0.1', 8000),
        http.server.SimpleHTTPRequestHandler
) as httpd:
    httpd.serve_forever()

# ターミナルからの起動
# import webbrowser
# webbrowser.open('http://127.0.0.1:8000')