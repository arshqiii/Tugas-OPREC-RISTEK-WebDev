from django import forms
from django.forms import ModelForm
from main.models import Tryout, Question

class TryoutForm(ModelForm):
    class Meta :
        model = Tryout
        fields = ['title', 'description']

class QuestionForm(ModelForm):
    ANSWER_CHOICES = [
        (True, 'True'),
        (False, 'False'),
    ]

    answer = forms.ChoiceField(
        choices=ANSWER_CHOICES,
        widget=forms.RadioSelect
    )
    class Meta:
        model = Question
        fields = ['text', 'answer']