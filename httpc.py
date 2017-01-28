"""Usage:
  httpc.py --help
  httpc.py get <url>
  httpc.py post [options] <url>

Options:
  --help                  Show this screen.
  -h, --header HEADERS    Headers of the request.
  -d, --data BODY         Body of the request.

"""
from docopt import docopt
from lab_assignment1 import http_get

if __name__ == '__main__':
    args = docopt(__doc__)  # parse arguments based on docstring above

    # determine the http request type, and call the appropriate function
    # python3 httpc.py get http://httpbin.org/get\?param\=value\&param2\=value2
    if(args.get("get")):
        http_get(args.get("<url>"))
    # if(args.get("post")):
    #     http_post()
