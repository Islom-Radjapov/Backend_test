from django.urls import path
from . import views



urlpatterns = [
    path('', views.GenderPradict.as_view()  )
]