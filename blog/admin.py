from django.contrib import admin
from .models import  Category, Article, Tag

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Tag)

