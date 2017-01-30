import socket
import sys
import argparse
from urllib.parse import urlparse

def http_get(url, port=80):
    # Retrieve hostname from passed URL
    host = urlparse(url).hostname

    # Format get query using URL and Host
    query = "GET %s HTTP/1.1\r\nHost: %s\n\r\n\r\n" % (url, host)

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((host, port))
        connection.sendall(query.encode("utf-8"))
        response = connection.recv(4096)
        sys.stdout.write(response.decode("utf-8"))
    finally:
        connection.close()

def http_post(headers, data, url, port=80):

    # Retrieve hostname from passed URL
    host = urlparse(url).hostname

    query = "POST /post HTTP/1.1\r\nHost: %s\n\r%s \n\r\n\r%s\n\r\n\r\n" % (host, headers, data)
    sys.stdout.write(query)

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((host, port))
        connection.sendall(query.encode("utf-8"))
        response = connection.recv(4096)
        sys.stdout.write(response.decode("utf-8"))
    finally:
        connection.close()
