from wsgiref.simple_server import make_server, demo_app

urls = {}

def handle_requests(environ, start_response):
    method = environ['REQUEST_METHOD'].upper() # get the request method
    path = environ['PATH_INFO'] 

    # then, lookup if there's a matching route:
    if path in urls:
        start_response('200 OK', [('content-type', 'text/html')])
        return urls["GET"][path]()
            
def run(urls):
    httpd = make_server('', 8000, handle_requests)
    print "Serving HTTP on http://localhost:8000"
    httpd.serve_forever()
