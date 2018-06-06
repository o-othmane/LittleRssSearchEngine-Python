#!/usr/bin/env python3 #For Unix
""" #!C:\Python34\python.exe #For Windows"""


"""
@author: Othmane Ouenzar, Soufiane Benhaddou
"""
import http.server, webbrowser

PORT = 8000

script_path = "src/search.py"

server_class = http.server.HTTPServer
handler_class = http.server.CGIHTTPRequestHandler
handler_class.cgi_directories = "/src"
server_address = ("", PORT)

httpd = server_class(server_address, handler_class)

url = 'http://localhost:{0}/{1}'.format(PORT, script_path)

webbrowser.open_new_tab(url)

print("serving at", url)

httpd.serve_forever()
