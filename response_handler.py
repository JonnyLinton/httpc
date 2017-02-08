import socket
import sys

def sendRequest(query, host, port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((host, port))
        connection.sendall(query.encode("utf-8"))
    finally:
        return connection

def getResponse(connection, verbose):
    try:
        response = receiveResponse(connection)
        printResponse(response, verbose)
    finally:
        connection.close()

def receiveResponse(connection):
    response = ""
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
