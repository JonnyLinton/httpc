#Installation
Requirements: pip (https://packaging.python.org/installing/#install-pip-setuptools-and-wheel)

`pip install -e .`

# Introducing httpc 1.0

httpc is a curl-like application but supports HTTP protocol only.

##Table of Contents
- [How to use httpc](#how-to-use-httpc)
- [get usage](#get-usage)
- [post usage](#post-usage)
- [Examples](#examples)
  - [get with verbose option](#get-with-verbose-option)
  - [post with inline data](#post-with-inline-data)

##How to use httpc
Using httpc is easy. Just type a command, like this
  `httpc command [arguments]`
The commands are:
- `get` : executes an HTTP GET request and prints the response
- `post` : executes a HTTP POST request and prints the response
- `help` : prints this README

Use `httpc help [command]` for more information about a specific command.

## Get Usage
Here's what a typical `get` command looks like:
`httpc get [-v] [-h key:value] URL`

Get executes an HTTP GET request for a given url

`-v` : Prints the details of the response such as protocol, status, and headers.

`-h key:value` : Associates headers to HTTP Request with the format `key:value`.

##Post Usage
Now here's how you would do a post request
`httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL`

Post executes a HTTP POST request for a given URL with inline data or from file.

`-v` : Prints the detail of the response such as protocol, status and headers.

`-h key:value` : Associates headers to HTTP request with the format `key:value`

`-d string` : Associates an inline data to the body HTTP POST request

`-f file` : Associates the content of a file to the body HTTP POST request.

Either `[-d]` or `[-f]` can be used but not both.

##Examples

`httpc get 'http://httpbin.org/get?course=networking&assignment=1'`

Output:

```
{
"args": {
    "assignment": "1",
    "course": "networking"
  },
  "headers": {
    "Host": "httpbin.org",
    "User-Agent": "Concordia-HTTP/1.0"
},
  "url": "http://httpbin.org/get?course=networking&assignment=1"
}
```

###Get with verbose option
`httpc get -v 'http://httpbin.org/get?course=networking&assignment=1'`

Output:

```
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 10 Sep 2016 15:53:19 GMT
Content-Type: application/json
Content-Length: 255
Connection: close
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
{
  "args": {
    "assignment": "1",
    "course": "networking"
  },
  "headers": {
    "Host": "httpbin.org",
    "User-Agent": "Concordia-HTTP/1.0"
    Comp445 – Lab Assignment # 1 Page 7 ©Aiman Hanna
},
  "url": "http://httpbin.org/get?course=networking&assignment=1"
}
```

###Post with inline data
`httpc post -h Content-Type:application/json --d '{"Assignment": 1}'
http://httpbin.org/post`

Output:

```
{
  "args": {},
  "data": "{\"Assignment\": 1}",
  "files": {},
  "form": {},
  "headers": {
    "Content-Length": "17",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "Concordia-HTTP/1.0"
}, "json": {
    "Assignment": 1
  },
  "url": "http://httpbin.org/post"
}
```
