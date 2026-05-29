def app(environ, start_response):
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]

    if method == "GET" and path == "/ping":
        status = "200 OK"
        headers = [("Content-Type", "text/plain")]
        start_response(status, headers)
        return [b"pong"]

    status = "404 Not Found"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return [b"Not Found"]