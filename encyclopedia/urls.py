from django.urls import path

from encyclopedia import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("new", views.new, name="new"),
    path("edit/<str:title>", views.edit, name="edit")
]
