"""Usage:
  httpc --help
  httpc get <url>
  httpc post [options] <url>

Options:
  --help                  Show this screen.
  -h, --headers HEADERS   Headers of the request.
  -d, --data BODY         Body of the request.

"""
from docopt import docopt
from lab_assignment1 import http_get, http_post

def run():
    args = docopt(__doc__)  # parse arguments based on docstring above
    # determine the http request type, and call the appropriate function
    if(args.get("get")):
        http_get(args.get("<url>"))
    if(args.get("post")):
        http_post(args.get("--headers"), args.get("--data"), args.get("<url>"))
