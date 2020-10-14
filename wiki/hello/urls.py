from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("bastian", views.bastian, name="bastian"),
    path("bastian/<str:name>", views.elfert, name="elfert"),
    path("<str:name>", views.greet, name="greet"),
]