"""Exemple Client"""

import socket

host = 'localhost'
port = 8000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall("Hello world2".encode('utf-8'))
    buff = s.recv(512)
    print(buff.decode())
