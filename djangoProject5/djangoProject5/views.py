from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def start(request):
#     return HttpResponse("<a href='app1'>to Board</a>")

def start(request):
    return HttpResponse("<a href='app1'>" +
                        "<button style='width:200px; background:red;'>" +
                        "to Board" +
                        "</button>" +
                        "</a><br>" +
                        "<a href='app1/many_insert'>" +
                        "<button style='width:200px; background:red;'>" +
                        "to many_insert" +
                        "</button>" +
                        "</a>"
                        )