import socket

def get(url, port=80):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((url, port))
        request = url.encode("utf-8")
        connection.sendall(request)
        response = connection.recv(len(request), socket.MSG_WAITALL)
        print(response)
    finally:
        connection.close()
