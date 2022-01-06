from django.contrib import admin

# Register your models here.
import member.models

admin.site.register(member.models.memberTable)