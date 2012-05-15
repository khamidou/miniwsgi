from __init__ import run

def myview(request):
    return "<h1>Hello world!</h1>"

urls = { 
    "/hello" : {"view": myview}
}

if __name__ == "__main__":
    run(urls)
