from django.http import HttpResponse


def index(request):
    return HttpResponse("<body bgcolor=green>" +
                        "<hr>" +
                        "<h1>첫 페이지 입니다.</h1>" +
                        "<hr>" +
                        "<a href=start>to start page</a><br>" +
                        "<a href=start2>to start2 page</a><br>" +
                        "<a href=admin>to admin page</a><br>" +
                        "<a href=start3>to start3 page</a><br>" +
                        "<a href=app5>to start5 page</a><br>" +
                        ## start3을 호출하면, 컨트롤러에서 100 + 300을 더해서
                        ## 100과 300을 더한 값은 400입니다.출력!!
                        ## app3.start3.html에 넣으면 됩니다.
                        "</body>")