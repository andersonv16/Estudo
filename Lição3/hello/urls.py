from django.urls import path

from . import views

urlpatterns = [
path ("", views.index, name="index"),
path ("Anderson", views.anderson, name="Anderson"),
path ("<str:name>", views.greet, name="greet")
]