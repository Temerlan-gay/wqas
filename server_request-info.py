def app(environ, start_response):
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]
    protocol = environ["SERVER_PROTOCOL"]

    if method == "GET" and path == "/info":
        response = f"""
Method: {method}
URL: {path}
Protocol: {protocol}
"""

        status = "200 OK"
        headers = [("Content-Type", "text/plain")]
        start_response(status, headers)
        return [response.encode()]

    status = "404 Not Found"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return [b"Not Found"]