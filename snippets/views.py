from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models import Employees
from .serializers import EmployeesSerializer
# Create your views here.

class Home(APIView):
    def get(self, request):
        return Response("HOME SNIPPETS")

class EmployeesViewSet(ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer