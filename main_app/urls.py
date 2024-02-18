from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path("survey/", views.choice, name='survey'),
    path('quiz/', views.quiz, name='quiz'),
    path('data/', views.data_view, name='data_view')

]