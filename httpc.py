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
from lab_assignment1 import http_get, http_post

def run():
    args = docopt(__doc__)  # parse arguments based on docstring above
    print(args.get("<command>"))

    if(args.get("help") and args.get("<command>")):
        exit(call(['python', 'httpc_%s.py' % args['<command>']]))

    # determine the http request type, and call the appropriate function
    elif(args.get("get")):
        http_get(args.get("<url>"), args.get("-v"))
    elif(args.get("post")):
        http_post(args.get("--headers"), args.get("--data"), args.get("<url>"), args.get("-v"))
