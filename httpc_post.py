from lab_assignment1 import sendRequest, getResponse, receiveResponse, printResponse
from urllib.parse import urlparse

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
