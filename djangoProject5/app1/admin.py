from django.contrib import admin

import app1.models

# Register your models here.
# 웹상에서 관리자모드로 볼 수 있도록
admin.site.register(app1.models.Board)
admin.site.register(app1.models.Reply)