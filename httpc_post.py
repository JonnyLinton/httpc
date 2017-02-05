"""
Usage: httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL

Post executes a HTTP POST request for a given URL with inline data or from file.

   -v               Prints the detail of the response such as protocol, status, and headers.
   -h key:value     Associates headers to HTTP Request with the format 'key:value'.
   -d string        Associates an inline data to the body HTTP POST request.
   -f file          Associates the content of a file to the body HTTP POST request.

Either [-d] or [-f] can be used but not both.
"""

from docopt import docopt

if __name__ == '__main__':
    print(docopt(__doc__))

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
