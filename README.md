# Introducing httpc 1.0

httpc is a curl-like application but supports HTTP protocol only.

##How to use httpc
Using httpc is easy. Just type a command, like this
  `httpc command [arguments]`
The commands are:
`get` : executes an HTTP GET request and prints the response
`post` : executes a HTTP POST request and prints the response
`help` : prints this README

Use `httpc help [command]` for more information about a specific command.

## Get Usage
`httpc help get`

usage: `httpc get [-v] [-h key:value] URL`

Get executes an HTTP GET request for a given url

`-v` : Prints the details of the response such as protocol, status, and headers.

`-h key:value` : Associates headers to HTTP Request with the format `key:value`.

##Post Usage
`httpc help post`

usage: `httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL`

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
