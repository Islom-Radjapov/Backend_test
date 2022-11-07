from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view()),
    # path('gender/', views.GenderPradict.as_view()),
]