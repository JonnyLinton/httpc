import socket
import sys

def sendRequest(query, host, port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((host, port))
        connection.sendall(query.encode("utf-8"))
    finally:
        return connection

def receiveResponse(connection):
    response = ""
    while True:
        try:
            connection.settimeout(0.2)
            response += connection.recv(1024).decode("utf-8")
        except:
            return response

def checkForRedirect(response):
    responseTemp = response
    headers = responseTemp.split("\r\n")
    code = int(headers[0].split(" ")[1])
    if(code > 299 and code < 400):
        for header in headers:
            if("Location:" in header):
                location = header.split(": ")[1]
        if(location):
            print("3xx type HTTP code given in response -- redirecting to ", location)
            return location
        else:
            print("No Location specified in the headers! Cannot redirect.")

def printResponse(response, verbose):
    if(verbose):
        print(response)
    else:
        # responseArr[0] contains headers, responseArr[1] contains body
        responseArr = response.split("\r\n\r\n")
        print(responseArr[1])
