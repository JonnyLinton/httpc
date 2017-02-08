"""
Usage: httpc post -v -h key:value -d inline-data -f file URL
Post executes a HTTP POST request for a given URL with inline data or from file.
   -v               Prints the detail of the response such as protocol, status, and headers.
   -h key:value     Associates headers to HTTP Request with the format 'key:value'.
   -d string        Associates an inline data to the body HTTP POST request.
   -f file          Associates the content of a file to the body HTTP POST request.
   -o FILE          Outputs response to specified file.
Either -d or -f can be used but not both.
"""

from response_handler import sendRequest, getResponse, receiveResponse, printResponse
from urllib.parse import urlparse
from docopt import docopt

if __name__ == '__main__':
    print(docopt(__doc__))

def http_post(headers, data, url, verbose, port=80):
    # Retrieve hostname from passed URL
    host = urlparse(url).hostname
    # encode data and convert to string so that the len() method works properly
    data_str = str(data).encode("utf-8")

    #Specify Connection and Content-Length in headers
    content_header = "Content-Length: " + str(len(data_str))
    query = "POST /post HTTP/1.1\r\nHost: %s\r\n%s\r\n%s\r\n\r\n%s" % (host, headers, content_header, data)
    connection = sendRequest(query, host, port)
    getResponse(connection, verbose)
