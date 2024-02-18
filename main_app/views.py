from django.shortcuts import render, HttpResponse
from .models import historicalModels,Quiz
import requests
import json
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import QuizQuestions
import random



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
            return render(request, 'main_app/map.html')
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


def about_view(request):
    return render(request, 'main_app/about.html')


def contact(request):
    return render(request, 'main_app/contact.html')


@csrf_exempt
def map_view(request):
    response = requests.get('https://data.calgary.ca/resource/99yf-6c5u.json')
    data = json.loads(response.text) if response.status_code == 200 else []
    indices = [random.randint(0, len(data)) for _ in range(15)]
    lastElement = Quiz.objects.last()
    random_number = random.randint(0, 2)
    if random_number == "0":
        indices.clear()
        match lastElement.horror:
            case "Cemetery":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "Cemetery" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)
            case "Warehouse":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "Warehouse" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)
            case "Hospital":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "Hospital" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)            
            case "Factory":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "Factory" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)            
            case "Hotel":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "Hotel" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)            
            case "Grocery Store":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "Shop" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)            
            case _:
                    indices = [random.randint(0, len(data)) for _ in range(15)]


    elif random_number == "1":
                indices.clear()
                match lastElement.profession:
                    case "Baker":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "Bakery" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)
                    case "Civil Engineer":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "Office" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)

                    case "Farmer":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "Farm" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)
                    case "Priest":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "Church" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)
                    case "Librarian":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "Library" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)
                    case "Teacher":
                        for item in data:
                            for index, item in enumerate(data):
                                if "typology" in item and "School" in item["typology"]:
                                    # Add the index to the array
                                    indices.append(index)
                    case _:
                        indices = [random.randint(0, len(data)) for _ in range(15)]
            # radom() NEED TO CODE
    else:
        indices.clear()
        if lastElement.bridges == True:
            for item in data:
                for index, item in enumerate(data):
                    if "typology" in item and "Bridge" in item["typology"]:
                        # Add the index to the array
                        indices.append(index)
        else:
            indices = [random.randint(0, len(data)) for _ in range(15)]

    # Process the first item (if it exists)
    if data:
        for index in indices: 
            item = data[index]
            if 'address' in item and ' AV ' in item['address']:
                item['address'] = item['address'].replace(' AV ', ' AVE ')
            if 'address' in item:
                item['address'] += ', Calgary'  


    return render(request, 'main_app/map.html', {'data': [item] if data else []})




