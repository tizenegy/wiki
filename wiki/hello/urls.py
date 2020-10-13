from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("bastian", views.bastian, name="bastian"),
    path("<str:name>", views.greet, name="greet"),
]