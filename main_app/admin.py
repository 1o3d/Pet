from django.contrib import admin
from .models import historicalModels, Quiz

admin.site.register(historicalModels)
admin.site.register(Quiz)