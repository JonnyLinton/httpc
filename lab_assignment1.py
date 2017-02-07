import socket
import sys
import argparse
from urllib.parse import urlparse

def http_get(url, verbose, port=80):
    # Retrieve hostname from passed URL
    host = urlparse(url).hostname

    # Format get query using URL and Host
    query = "GET %s HTTP/1.1\r\nHost: %s\n\r\n\r\n" % (url, host)

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((host, port))
        connection.sendall(query.encode("utf-8"))
        response = receiveResponse(connection)
        printResponse(response, verbose)
    finally:
        connection.close()
def http_post(headers, data, url, verbose, port=80):

    # Retrieve hostname from passed URL
    host = urlparse(url).hostname

    #Specify Connection and Content-Length in headers
    content_header = "Content-Length: " + str(len(data))
    query = "POST /post HTTP/1.1\r\nHost: %s\r\n%s\r\n%s\r\n\r\n%s" % (host, headers, content_header, data)

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((host, port))
        connection.sendall(query.encode("utf-8"))
        response = receiveResponse(connection)
        printResponse(response, verbose)
    finally:
        connection.close()
def receiveResponse(connection):
    response = ""
    while True:
        response += connection.recv(32).decode("utf-8")
        # if all the headers have been read
        if("\r\n\r\n" in response):
            responseSize = response.split("Content-Length: ")[1].split("\r\n")[0]
            responseSize = int(responseSize)
            while True:
                try:
                    connection.settimeout(0.2)
                    response += connection.recv(1024).decode("utf-8")
                except:
                    return response

def printResponse(response, verbose):
    if(verbose):
        print(response)
    else:
        # responseArr[0] contains headers, responseArr[1] contains body
        responseArr = response.split("\r\n\r\n")
        print(responseArr[1])
