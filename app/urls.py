from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ques_id>/', views.qna, name='QnA'),
]