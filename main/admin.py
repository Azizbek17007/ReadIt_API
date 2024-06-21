from django.contrib import admin
from django.contrib.admin import site

# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'content')
    list_display_link = ('id','title', 'author', 'content')
    search_fields = ('title', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(TagModel)
admin.site.register(CategoryModel)
admin.site.register(AuthorModel)
admin.site.register(Post)

