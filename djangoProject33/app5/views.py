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

def js06(request):
    print('js06 함수 호출')
    return render(request, "app5/js06.html")

def js07(request):
    print('js07 함수 호출')
    return render(request, "app5/js07.html")

def js08(request):
    print('js08 함수 호출')
    return render(request, "app5/js08.html")

def js09(request):
    print('js09 함수 호출')
    return render(request, "app5/js09.html")

def js10(request):
    print('js10 함수 호출')
    # db연동 결과를 검색해서 가지고 온다.
    # 결과를 html에 보내주어야 한다. => dictionary 형태
    context = {'userName': 'hong',
               'field': 'shoes',
               'email': 'wsong15@hawk.iit.edu',
               'contact': '010-4904-2996',
               'payValue': 5000}
    return render(request, "app5/js10.html", context)

def js100(request):
    print('js100 함수 호출')
    # db연동 결과를 검색해서 가지고 온다.
    # 결과를 html에 보내주어야 한다. => dictionary 형태
    context = {'site': [100, 200, 300],
               'url': {'u1': 'naver', 'u2': 'daum', 'u3': 'google'},
               'name': ['hong', 'kim', 'apple'],
               }
    return render(request, "app5/js100.html", context)

def map1(request):
    print('map1 함수 호출')
    # 3 장소의 위도 경도를 만들어서,
    # comments = ['영등포 타임스퀘어', '신촌역 이마트', '도봉산']
    lats = [37.51725181697697, 37.560260, 37.689447]
    lngs = [126.90373968262504, 126.942149, 127.046558]
    context = {"latitude": lats,
               "longitude": lngs,}
    return render(request, "app5/map1.html", context)

def map2(request):
    print('map2 함수 호출')
    return render(request, "app5/map2.html")

def chart1(request):
    print('chart1 함수 호출')
    return render(request, "app5/chart1.html")