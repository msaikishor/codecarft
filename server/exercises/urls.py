from django.urls import path
from . import views

urlpatterns = [
    path('exercises/', views.exercise_list, name='exercise_list'),
    path('exercise/<int:id>/', views.exercise_detail, name='exercise_detail'),
]
