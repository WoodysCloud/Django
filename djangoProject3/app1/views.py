from django.shortcuts import render

# Create your views here.
def start(request):
    print('start함수 호출됨.')
    data = {"name" : "park", "age" : 100}
    #html에 넣고 싶은 데이터가 있으면 dic로 만들어주어라.!
    return render(request, "app1/start.html", data)