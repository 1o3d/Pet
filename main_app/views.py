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