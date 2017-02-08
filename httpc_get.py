"""
Usage: httpc get [-v] [-h key:value] URL
Get executes a HTTP GET request for a given URL.
   -v             Prints the detail of the response such as protocol, status, and headers.
   -h key:value   Associates headers to HTTP Request with the format 'key:value'.
"""

from lab_assignment1 import sendRequest, getResponse, receiveResponse, printResponse
from urllib.parse import urlparse
from docopt import docopt

if __name__ == '__main__':
    print(docopt(__doc__))

def http_get(url, verbose, port=80):
    # Retrieve hostname from passed URL
    host = urlparse(url).hostname

    # Format get query using URL and Host
    query = "GET %s HTTP/1.1\r\nHost: %s\n\r\n\r\n" % (url, host)
    connection = sendRequest(query, host, port)
    getResponse(connection, verbose)
