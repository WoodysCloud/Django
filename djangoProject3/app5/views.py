from django.shortcuts import render

# Create your views here.
def start5(request):
    print('start5 함수 호출')
    context = {"today" : "금요일",
               "when" : "2022년 1월 7일"}
    return render(request, "app5/start5.html", context)

def js01(request):
    print('js01 함수 호출')
    return render(request, "app5/js01.html")

def js02(request):
    print('js02 함수 호출')
    return render(request, "app5/js02.html")

def js03(request):
    print('js03 함수 호출')
    return render(request, "app5/js03.html")

def js04(request):
    print('js04 함수 호출')
    return render(request, "app5/js04.html")

def js05(request):
    print('js05 함수 호출')
    return render(request, "app5/js05.html")

def js05_1(request):
    print('js05_1 함수 호출')
    return render(request, "app5/js05_1.html")