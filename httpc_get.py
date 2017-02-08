"""
Usage: httpc get [-v] [-h key:value] URL
Get executes a HTTP GET request for a given URL.
   -v             Prints the detail of the response such as protocol, status, and headers.
   -h key:value   Associates headers to HTTP Request with the format 'key:value'.
   -o FILE        Outputs response to specified file.
"""

from message_handler import sendRequest, getResponse, receiveResponse, printResponse
from urllib.parse import urlparse
from docopt import docopt

if __name__ == '__main__':
    print(docopt(__doc__))

def http_get(url, verbose, headers, port=80):
    # Retrieve hostname from passed URL
    host = urlparse(url).hostname

    # Transform list of headers into single string, separated by \r\n
    formattedHeaders = "\r\n".join(headers)

    # Format get query using URL and Host
    query = "GET %s HTTP/1.1\r\nHost: %s\r\n%s\n\r\n\r\n" % (url, host, formattedHeaders)
    connection = sendRequest(query, host, port)
    getResponse(connection, verbose)
