from django.shortcuts import render, HttpResponse
from .models import historicalModels
import requests
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import QuizQuestions


# Create your views here.
def index(request):
    return render(request, 'main_app/homepage.html')


def choice(request):
    print('This is a', request.method)
    if request.method == 'POST':
        action = request.POST.get("action")
        if action == "Survey":
            return render(request, 'Survey.html')
        if action == "Random":
            return render(request, "Random.html")


@csrf_exempt
def quiz(request):
    if request.method == 'POST':
        form = QuizQuestions(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuizQuestions()
    return render(request, 'main_app/quiz.html', {'form': form})

def data_view(request):
    response = requests.get('https://data.calgary.ca/resource/99yf-6c5u.json')
    data = json.loads(response.text) if response.status_code == 200 else []
    for item in data:
        if 'address' in item and ' AV ' in item['address']:
            item['address'] = item['address'].replace(' AV ', ' AVE ')
        if 'address' in item:
            item['address'] += ', Calgary'     
    return render(request, 'data.html', {'data': data})