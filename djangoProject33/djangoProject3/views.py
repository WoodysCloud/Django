from django.http import HttpResponse

def index(request):
    return HttpResponse("<body bgcolor=gold>" +
                        "<hr>" +
                        "<h1>Main Page</h1>" +
                        "<hr>" +
                        "<a href=start>to start page</a><br>" +
                        "<a href=start2>to start2 page</a><br>" +
                        # "<a href=start3>to start3 page</a><br>" +
                        "<a href=admin>to admin page</a><br>" +
                        "<a href=app5>to app5 page</a><br>" +
                        "</body>")