from django.contrib import admin
from django.urls import path, re_path
from articles.views import archive, get_article, create_post, login_user, logout_user, register_user
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", archive, name="archive"),
    re_path(r"^article/(?P<article_id>\d+)/$", get_article, name="get_article"),
    path('article/new/', create_post, name='create_post'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
]
