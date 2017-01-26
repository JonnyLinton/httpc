import socket
from urllib.parse import urlparse

def get(url, port):
    host = urlparse(url).hostname
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((host, port))
        request = url.encode("utf-8")
        connection.sendall(request)
        response = connection.recv(len(request), socket.MSG_WAITALL)
        print(response.decode("utf-8"))
    finally:
        connection.close()

get("http://httpbin.org/get?course=networking&assignment=1", 80)
