# Introducing httpc 1.0

httpc is a curl-like application but supports HTTP protocol only.

##How to use httpc
Using httpc is easy. Just type a command, like this
  httpc command [arguments]
The commands are:
- get
 - executes an HTTP GET request and prints the response
- post
  - executes a HTTP POST request and prints the response
- help
  - prints this README

Use "httpc help [command]" for more information about a specific command.

## Get Usage
  httpc help get

  usage: httpc get [-v] [-h key:value] URL

Get executes an HTTP GET request for a given url

- -v
 - Prints the details of the response such as protocol, status, and headers.

- -h key:value
 - Associates headers to HTTP Request with the format 'key:value'.

##Post Usage
