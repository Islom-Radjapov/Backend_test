from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Employees

class EmployeesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()

    # class Meta:
    #     model = Employees
    #     fields = ()
def encode():
    model_sr = EmployeesSerializer('bir', 'content: ikki')
    # print(model_sr.data, type(model_sr.data), sep='\n')
    # json = JSONRenderer().render(model_sr)
    print(model_sr)
