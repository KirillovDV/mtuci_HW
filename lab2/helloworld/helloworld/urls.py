from django.contrib import admin
from django.urls import path
from flatpages.views import home

urlpatterns = [
    path("", home, name="home"),
    path("hello/", home, name="hello"),
    path("admin/", admin.site.urls),
]