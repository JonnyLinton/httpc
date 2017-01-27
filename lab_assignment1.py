import socket
import sys
from urllib.parse import urlparse

def get(url, port=80):
    # Retrieve hostname from passed URL
    host = urlparse(url).hostname
    # Retrieve query from URL
    query_parameters = urlparse(url).query
    full_get_query = "GET %s HTTP/1.1\r\nHost: %s\n\r\n\r\n" % (url, host)
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((host, port))
        connection.sendall(full_get_query.encode("utf-8"))
        response = connection.recv(4096)
        sys.stdout.write(response.decode("utf-8"))
    finally:
        connection.close()

get("https://httpbin.org/")
