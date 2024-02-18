from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path("survey/", views.choice, name='survey'),
    path('quiz/', views.quiz, name='quiz'),
    path('data/', views.data_view, name='data_view'),
    path('about/', views.about_view, name='about_view'),
    path('contact/', views.contact, name='contact')

]