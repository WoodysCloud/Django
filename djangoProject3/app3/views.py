from django.shortcuts import render

# Create your views here.
def start3(request):
    print('받은 데이터 n1>>  ', request.GET['n1'])
    print('받은 데이터 n2>>  ', request.GET['n2'])
    print('받은 데이터 subject>>  ', request.GET['subject'])
    print('start3함수 호출됨.')
    n1 = int(request.GET['n1'])
    n2 = int(request.GET['n2'])
    result = n1 + n2
    # context = {"result" : request.GET['n1'] + request.GET['n2']}
    context = {"result" : result,
               "n1" : n1,
               "n2" : n2,
               "subject": request.GET['subject']
    }
    return render(request, "app3/start3.html", context)