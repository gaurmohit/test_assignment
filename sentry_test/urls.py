from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.errors_index, name="index"),
]