"""Usage:
  httpc help <command>
  httpc --help
  httpc get [-v] <url>
  httpc post [-v] [options] <url>

Options:
  --help                  Show this screen.
  -v                      Prints details of the response such as protocol, status, and headers
  -h, --headers HEADERS   Headers of the request.
  -d, --data BODY         Body of the request.

See 'httpc help <command>' for more information on a specific command.
"""
from docopt import docopt
from subprocess import call
# from lab_assignment1 import http_get, http_post
from httpc_get import http_get
from httpc_post import http_post

def run():
    args = docopt(__doc__)  # parse arguments based on docstring above

    if(args.get("help") and args.get("<command>")):
        command_help(args.get("<command>"))
    # determine the http request type, and call the appropriate function
    elif(args.get("get")):
        http_get(args.get("<url>"), args.get("-v"))
    elif(args.get("post")):
        http_post(args.get("--headers"), args.get("--data"), args.get("<url>"), args.get("-v"))
    else:
        "Invalid query"


def command_help(command):
    if command == "get":
        print("""Usage: httpc get [-v] [-h key:value] URL

Get executes a HTTP GET request for a given URL.
-v             Prints the detail of the response such as protocol, status, and headers.
-h key:value   Associates headers to HTTP Request with the format 'key:value'.""")
    elif command == "post":
        print("""
Usage: httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL

Post executes a HTTP POST request for a given URL with inline data or from file.

    -v               Prints the detail of the response such as protocol, status, and headers.
    -h key:value     Associates headers to HTTP Request with the format 'key:value'.
    -d string        Associates an inline data to the body HTTP POST request.
    -f file          Associates the content of a file to the body HTTP POST request.

Either [-d] or [-f] can be used but not both.
        """)
    else:
        print("httpc: Invalid command")
