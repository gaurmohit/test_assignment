from django.urls import include, path
from .views import show, save, show_all

urlpatterns = [
    path('show/<str:yname>/', show, name='show'),
    path('save/<str:yname>/', save, name='save'),
    path('showall/', show_all, name='showall'),
]