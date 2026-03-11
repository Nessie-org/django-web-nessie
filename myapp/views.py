from django.shortcuts import HttpResponse

def home(request):
    html = """
    <html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Welcome to the Home Page!</h1>
        <p>This is a simple Django view rendering an HTML template.</p>
    </body>
    </html>
    """
    return HttpResponse(html)
