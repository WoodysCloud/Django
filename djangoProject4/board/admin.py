from django.contrib import admin

# Register your models here.
import board.models

admin.site.register(board.models.boardTable)