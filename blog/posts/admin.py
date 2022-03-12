from django.contrib import admin
from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id','created_by','meta_title','slug','status')

admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id','category_title','category_slug')

admin.site.register(Category,CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_id','tag_title','tag_content')

admin.site.register(Tag,TagAdmin)



