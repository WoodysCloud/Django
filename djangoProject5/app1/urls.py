from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

# http://127.0.0.1:9999/app1
import app1.views

urlpatterns = [
    path('', app1.views.index, name='index'),
    path('/list', app1.views.list, name='list'), # 전체목록 조회, R
    path('/insert', app1.views.insert, name='insert'), # 게시물 생성, C
    path('/insert2', app1.views.insert2, name='insert2'),
    path('/insert3', app1.views.insert3, name='insert3'), # 댓글 추가용
    path('/one/<id>', app1.views.one, name='one'), # 한개목록 조회, R
    path('/delete/<id>', app1.views.delete, name='delete'), # 게시물 삭제, D
    path('/update/<id>', app1.views.update, name='update'), # 게시물 수정화면1, U
    path('/update2', app1.views.update2, name='update2'), # 게시물 수정화면2, U
    path('/many_insert', app1.views.many_insert, name='many_insert'),
]