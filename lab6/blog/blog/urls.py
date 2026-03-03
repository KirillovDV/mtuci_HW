from django.contrib import admin
from django.urls import path, re_path
from articles.views import archive, get_article
from articles.views import archive, get_article, create_post

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", archive, name="archive"),
    re_path(r"^article/(?P<article_id>\d+)/$", get_article, name="get_article"),
    path('article/new/', create_post, name='create_post'),
]