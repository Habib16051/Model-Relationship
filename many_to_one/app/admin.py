from django.contrib import admin
from . models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_name', 'post_cat', 'post_publish_date', 'user']
