from django.shortcuts import render

# Create your views here.
def start(request):
    print('start 함수 호출')
    data = {"name" : "park", "age" : 100}
    # html에 넣고 싶은 데이터가 있으면 dictionary로 만들어줄 것
    return render(request, "app1/start.html", data)