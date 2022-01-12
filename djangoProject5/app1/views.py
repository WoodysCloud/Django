from django.shortcuts import render, redirect

# Create your views here.
from app1.models import Board


def index(request):
    return render(request, 'app1/index.html')

def list(request):
    print('list함수 호출됨.')

    # board 테이블에서 전체 리스트를 검색해서 가지고 온다.
    board_list = Board.objects.order_by('-id') # db에 게시판은 위에서 아래로 순서대로 생성되지만 보여줄 땐 최근게시물이 맨 위로! => 역순으로!
    print('db에서 가지고 온 data>> ', board_list)

    # 가지고 온 데이터를 dictionary로 만들어준다.
    context = {
        'list' : board_list
    }

    # 데이터를 넣어서 보내줄 template지정, 데이터를 넘겨줌.
    return render(request, 'app1/list.html', context)

def one(request, id):
    print("받은 id >> ", id)

    # id를 가지고 검색해주세요.
    one = Board.objects.get(id=id)

    # dictionary로 만들어주세요.
    context = {
        "one" : one
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