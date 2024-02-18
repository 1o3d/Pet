from django import forms
from . import models


class QuizQuestions(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = ['zodiac', 'horror', 'bridges', 'profession']