from django.shortcuts import render
from django.views.generic import ListView
from .models import Add_news
# Create your views here.

class HomePageView(ListView):
    model = Add_news
    template_name = 'home_news.html'