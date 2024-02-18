from django.shortcuts import render, HttpResponse
from .models import historicalModels
import requests
import json

# def index(request):
#     return render(request, 'homepage.html')




def data_view(request):
    response = requests.get('https://data.calgary.ca/resource/99yf-6c5u.json')
    data = json.loads(response.text) if response.status_code == 200 else []
    return render(request, 'data.html', {'data': data})
