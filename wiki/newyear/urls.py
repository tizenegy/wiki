from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("yourmum", views.yourmum, name="yourmum"),
    path("lisa/<str:name>", views.lisa, name="lisa"),
    path("<str:name>", views.hismum, name="hismum"),
]
