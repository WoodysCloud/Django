from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from app5.models import Test

def delete(request, id):
    print('삭제할 id는>> ', id)
    one = Test.objects.get(id=id)
    one.delete()
    print(id , '삭제됨.================')
    v
    #redirect는 서버가 클라이언트에게 해당주소를 요청하도록 명령함.

def update(request, id): # 수정할 수 있는 화면을 호출하는 함수
    print('수정할 id는>> ', id)
    one = Test.objects.get(id=id) #db검색후, template파일에 넘겨주세요.
    context = {
        'one' : one
    }
    return render(request, "app5/update.html", context)

def update2(request): # 수정될 데이터 받아서 db에 update처리하는 함수
    data = request.POST
    print('수정할 데이터들>> ', data)
    #검색을 먼저 한다음에,
    one = Test.objects.get(id = data.get('id'))
    #특정한 컬럼값 변경해주고,
    one.name = data.get('name')
    one.tel = data.get('tel')
    one.addr = data.get('addr')
    one.save()
    # 전체목록페이지를 호출해주자.
    return redirect('/app5/test')

def person(request, id):
    print('받은 id는>> ' , id)
    # db검색해주세요.
    one = Test.objects.get(id = id)
    # 검색한 결과를 dic로 만들어주세요.
    context = {
        'one' : one
    }
    # person.html을 만들어서 dic를 넘겨주세요.
    return render(request, "app5/person.html", context)
    # person.html에 개인 정보를 넣어주세요.

def test(request):
    test_list = Test.objects.order_by('-name')[:10]
    print('검색한 결과 >> ' ,  test_list)
    print('검색한 결과 >> ', test_list[0])
    context = {
        "test_list" : test_list
    }
    return render(request, "app5/test.html", context)

# Create your views here.
def start5(request):
    print('==================== start5호출됨.')
    context = {"today" : "금요일", "when" : "2022년 1월 7일"}
    return render(request, "app5/start5.html", context)

def js01(request):
    print('=================== js01호출됨.')
    return render(request, "app5/js01.html")

def js02(request):
    print('=================== js02호출됨.')
    return render(request, "app5/js02.html")

def js03(request):
    print('=================== js03호출됨.')
    return render(request, "app5/js03.html")

def js04(request):
    print('=================== js04호출됨.')
    return render(request, "app5/js04.html")

def js05(request):
    print('=================== js05호출됨.')
    return render(request, "app5/js05.html")

def js06(request):
    print('=================== js06호출됨.')
    return render(request, "app5/js06.html")

def js07(request):
    print('=================== js07호출됨.')
    return render(request, "app5/js07.html")

def js08(request):
    print('=================== js08호출됨.')
    return render(request, "app5/js08.html")

def js09(request):
    print('=================== js09호출됨.')
    return render(request, "app5/js09.html")

def js10(request):
    print('=================== js10호출됨.')
    #db연동 결과를 검색해서 가지고 온다.
    #결과를 html에 보내주어야 한다.
    context = {'userName': 'hong',
               'field' : 'shoes',
               'email' : 'aliciawill@kakao.com',
               'contact' : '010-4904-2996',
               'payValue' : 5000
               }
    return render(request, "app5/js10.html", context)

def js100(request):
    print('=================== js100호출됨.')
    #db연동 결과를 검색해서 가지고 온다.
    #결과를 html에 보내주어야 한다.
    context = {'site': [100, 200, 300],
               'url' : {'u1': 'naver', 'u2': 'daum', 'u3': 'google'},
               'name' : ['hong', 'kim', 'apple'],
               }
    return render(request, "app5/js100.html", context)

def map1(request):
    print('=================== map1호출됨.')
    # 3장소의 위도 경도를 만들어서, html에 표시
    location = """
    lats = [ 37.5705805429368, 37.560260, 37.689447 ]
    lngs = [ 126.99212654046664, 126.942149, 127.046558 ]
    """
    context = {'location' : location }
    return render(request, "app5/map1.html", context)

def map2(request):
    print('=================== map2호출됨.')
    # 37.51725181697697, 126.90373968262504
    return render(request, "app5/map2.html")

def ajax0(request):
    print('=================== ajax0호출됨.')
    return render(request, "app5/ajax0.html")

def ajax1(request):
    print('=================== ajax1호출됨.')
    return render(request, "app5/ajax1.html")

def target0(request):
    print('=================== target0호출됨.')
    context = {'result' : 100, 'sum' : 1000}
    return render(request, "app5/target0.html", context)

def target00(request):
    print('=================== target00호출됨.')
    context = {'today': -10, 'today2': 'bad'}
    return render(request, "app5/target00.html", context)

def target(request):
    print('=================== target호출됨.')
    data = request.GET
    print(data)
    print(data['name'], data['song'])
    context = {'result' : 100, 'age' : '한글이야.', 'tel' : [100, 200, 300]}
    # return render(request, "app5/target.html", context)
    # return HttpResponse(context)
    return JsonResponse(context)

def ajax2(request):
    print('=================== ajax2호출됨.')
    return render(request, "app5/ajax2.html")

def target2(request): #종로3가 위도, 경도
    print('=================== target2호출됨.')
    context = {"lat" : 37.570580, "lng" : 126.99212654}
    return JsonResponse(context)

def target3(request): #동대문 위도, 경도
    print('=================== target3호출됨.')
    context = {"lat" : 37.5642135, "lng" : 127.0016985}
    return JsonResponse(context)