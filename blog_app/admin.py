from django.contrib import admin
from blog_app.models import CreateBlog
# Register your models here.


@admin.register(CreateBlog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js')
