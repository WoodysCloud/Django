from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app1.models import Board, Reply


def index(request):
    return render(request, 'app1/index.html')

def list(request):
    print('list함수 호출됨.')

    # board 테이블에서 전체 리스트를 검색해서 가지고 온다.
    page = request.GET.get('page', 1) # 게시판 페이지 기능 추가
    board_list = Board.objects.order_by('-id') # db에 게시판은 위에서 아래로 순서대로 생성되지만 보여줄 땐 최근게시물이 맨 위로! => 역순으로!
    print('db에서 가지고 온 data>> ', board_list)

    # 가지고 온 데이터를 dictionary로 만들어준다.
    paginator = Paginator(board_list, 5) # 5개씩 1페이지에.. paginator 객체 생성
    page_obj = paginator.get_page(page) # 각 해당 페이지만
    context = {
        'list' : page_obj
    }

    # 데이터를 넣어서 보내줄 template지정, 데이터를 넘겨줌.
    return render(request, 'app1/list.html', context)

def one(request, id): # 상세페이지
    print("받은 id >> ", id) # id: 게시판 번호(auto increased)

    # id를 가지고 검색해주세요.
    one = Board.objects.get(id=id)

    # bid를 가지고 댓글 검색
    list = Reply.objects.filter(bid=id) # 여러개 받아올 땐 filter()

    # dictionary로 만들어주세요.
    context = {
        "one" : one,
        "list" : list
    }

    # template에 넣어주세요.
    return render(request, 'app1/one.html', context)

def insert(request):
    return render(request, 'app1/insert.html')

def insert2(request):
    data = request.POST
    print(data)
    print("게시물의 title >> ", data.get('title'))
    print("게시물의 content >> ", data.get('content'))
    print("게시물의 writer >> ", data.get('writer'))

    # 받은 데이터 db에 저장
    title = data.get('title')
    content = data.get('content')
    writer = data.get('writer')
    board = Board(title=title, content=content, writer=writer)

    # 객체 생성 -> save()
    board.save()
    return redirect('/app1/list')

def insert3(request):

    data = request.GET

    print(data)
    print("댓글의 bid >> ", data.get('bid'))
    print("댓글의 content >> ", data.get('content'))
    print("댓글의 writer >> ", data.get('writer'))

    bid = data.get('bid')
    content = data.get('content')
    writer = data.get('writer')
    reply = Reply(bid=bid, content=content, writer=writer)
    reply.save()

    # ajax로는 redirect 불가
    return HttpResponse('- <img src="/static/IMG_6380.jpeg" width="20" height="20">' +
                        content + '(' + writer + ')<br>')

def delete(request, id):
    print("받은 id는 >> ", id)

    # id로 검색
    one = Board.objects.get(id=id)

    # 삭제
    one.delete()
    print("삭제완료 id는 >> ", id)

    # 다음페이지를 게시판 리스트 페이지로 호출
    return redirect('/app1/list')

def update(request, id):
    print("받은 id는 >> ", id)

    # 받은 id로 db에서 데이터 가져오기
    one = Board.objects.get(id=id)

    # dictionary로 만든 데이터 template으로
    context = {
        "one" : one
    }
    return render(request, 'app1/update.html', context) # template으로 연결 => 맨앞에 '/' 필요없음

def update2(request):
    data = request.POST
    id = data.get('id')
    title = data.get('title')
    content = data.get('content')
    writer = data.get('writer')

    # 수정할땐 미리 검색 한번
    row = Board.objects.get(id=id)

    # 해당 컬럼값 변경
    row.title = title
    row.content = content
    row.writer = writer

    # 수정된 것 저장
    row.save()
    return redirect('/app1/list') # url 주소 => '/' 부터 입력

def many_insert(request):
    for i in range(300):
        b = Board(title='title' + str(i),
                  content='content' + str(i),
                  writer='user' + str(i))
        b.save()
    return redirect('/app1/list')