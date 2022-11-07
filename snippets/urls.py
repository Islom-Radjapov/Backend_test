from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'autors', views.EmployeesViewSet)


urlpatterns = [
    path('', views.Home.as_view()),
    path('', include(router.urls))
]