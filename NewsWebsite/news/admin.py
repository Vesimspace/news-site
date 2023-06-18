from django.contrib import admin
from news.models import Article, AppUser, Comment

admin.site.register(Article)
admin.site.register(AppUser)
admin.site.register(Comment)
