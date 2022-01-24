import random

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from mainPage.models import Good

from mainPage.models import Interior_obj, Board, Comment


def main(request):
    print('mainPage 호출됨')
    goods_list = Good.objects.all()
    mood = list(Interior_obj.objects.filter(individuality=1))
    moodpick = random.sample(mood, 10)
    objpick = Interior_obj.objects.order_by('-enfj')[:10]
    
    context = {'mbti': ['ENFJ','ENFP','ENTJ','ENTP','ESFJ',
                 'ESFP','ESTJ','ESTP','INFJ','INFP',
                 'INTJ','INTP','ISFJ','ISFP','ISTJ','ISTP'],
               'goods' : goods_list,
               'mood': moodpick,
               'obj': objpick,
               }
    return render(request, 'mainPage/main.html',context)

def scroll(request):
    goods_list = Good.objects.all()
    context = {'mbti': ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ',
                        'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP',
                        'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP'],
               'goods': goods_list
               }
    return render(request, 'mainPage/scroll.html',context)

def target(request):
    goods_list = Good.objects.all()
    context = {
               'goods': serializers.serialize('json', goods_list)
               }
    return JsonResponse(context)

def community(request):
    print('게시판')

    board_list = Board.objects.order_by('-id')
    print("게시물 전체 조회 >> ", board_list)

    context = {
        'board': board_list,
    }
    return render(request, 'mainPage/community.html', context)

def comment(request):
    print('view all comments')

    comments = Comment.objects.order_by('-id')
    print("댓글 전체 조회 >> ", comments)

    context = {
        'comments': comments,
    }

    return render(request, 'mainPage/comment.html', context)