import socket
import sys
from urllib.parse import urlparse

def get(url, port=80):
    # Retrieve hostname from passed URL
    host = urlparse(url).hostname
    # Retrieve query from URL
    query = urlparse(url).query
    good_query = "GET /?%s HTTP/1.1\r\nHost: %s\n\r\n\r\n" % (query, host)
    print(good_query)
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((host, port))
        connection.sendall(good_query.encode("utf-8"))
        response = connection.recv(8192, socket.MSG_WAITALL)
        sys.stdout.write(response.decode("utf-8"))
    finally:
        connection.close()

get("http://httpbin.org/get?course=networking&assignment=1")
