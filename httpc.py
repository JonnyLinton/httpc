"""Usage:
  httpc help <command>
  httpc --help
  httpc get [-v] <url>
  httpc post [-v] -h HEADERS (-d DATA | -f FILE) <url>

Options:
  --help                  Show this screen.
  -v                      Prints details of the response such as protocol, status, and headers
  -h, --headers HEADERS   Headers of the request.
  -d, --data BODY         Body of the request.
  -f, --file FILE         File containing the body of the request

See 'httpc help <command>' for more information on a specific command.
"""
from docopt import docopt
from subprocess import call
from httpc_get import http_get
from httpc_post import http_post

def run():
    args = docopt(__doc__)  # parse arguments based on docstring above

    if(args.get("help") and args.get("<command>")):
        exit(call(['python3', 'httpc_%s.py' % args.get("<command>")]))
    # determine the http request type, and call the appropriate function
    elif(args.get("get")):
        http_get(args.get("<url>"), args.get("-v"))
    elif(args.get("post")):
        filePath = args.get("--file")
        if(filePath):
            with open(filePath) as f:
                data = ""
                for line in f:
                    data += line
            http_post(args.get("--headers"), data, args.get("<url>"), args.get("-v"))
        else:
            http_post(args.get("--headers"), args.get("--data"), args.get("<url>"), args.get("-v"))
    else:
        "Invalid query"
