from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("wiki", views.search, name="search"),
    path("random", views.rdom, name="rdom")
]
