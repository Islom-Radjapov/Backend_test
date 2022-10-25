from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import wikipedia

wikipedia.set_lang("uz")
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
def wiki(request):
    if request.method == 'POST':
        data = json.load(request.body)
        print("__________________________________________________________POST",data)
        wikiped = wikipedia.page(data)
        print(wikiped)

        response = {'Wikipediya': f'{wikiped[:146]}'}
    else:
        print("______________________________________________________________ELSE")
        print(request)
        response = {'Wikipediya': 'POST request jonating!'}
    return JsonResponse(response, safe=True)

