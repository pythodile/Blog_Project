from django.contrib import admin
from .models import *
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('created_at','commented_by')


admin.site.register(Comment,CommentAdmin)
