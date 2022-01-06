from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def start(req): # views 내에 정의된 함수는 반드시 parameter 하나 (이상) 필요.
    # client가 입력한 data를 받아주기 위한 변수
    print('start 함수 호출') # 터미널에 나올듯
    # client에게 처리결과를 주어야 하기 때문에 "return"으로
    return HttpResponse("<body bgcolor=gold><h1>" +
                        "I am a start page..<br>" +
                        "<a href='http://www.google.com'>to google</a><br>" +
                        "<a href='http://127.0.0.1:8000/start2'>to start2</a><br>" +
                        "<a href='http://www.cafe.daum.net/bigmeta'>to bigmeta</a><br>" +
                        "<a href='http://127.0.0.1:8000/start3'>to start3</a><br>" +
                        "</h1></body>") # html로 변형시켜줌
    # 자동 import: 해당 라이브러리위에서 alt + enter 실행

def start2(req):
    print('start2 함수 호출')
    return HttpResponse('<font color=red>I am a start2 page..</font>')

def start3(req):
    print("start3 함수 호출")
    return HttpResponse('<h1><a href="http://127.0.0.1:8000">to main</a><br>' +
                        '<a href="http://127.0.0.1:8000/start2">to start2</a></h1>')