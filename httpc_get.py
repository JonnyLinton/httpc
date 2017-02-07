from lab_assignment1 import sendRequest, getResponse, receiveResponse, printResponse
from urllib.parse import urlparse

def http_get(url, verbose, port=80):
    # Retrieve hostname from passed URL
    host = urlparse(url).hostname

    # Format get query using URL and Host
    query = "GET %s HTTP/1.1\r\nHost: %s\n\r\n\r\n" % (url, host)
    connection = sendRequest(query, host, port)
    getResponse(connection, verbose)
