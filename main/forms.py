from django import forms
from django.forms import ModelForm
from main.models import Tryout, Question

class TryoutForm(ModelForm):
    class Meta :
        model = Tryout
        fields = ['title', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'border-4 border-gray-700 p-2 rounded-lg w-full'}),
            'category': forms.Select(attrs={'class': 'border-10 border-gray-700 p-2 rounded-lg w-full'}),
        }

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
        widgets = {
            'text': forms.TextInput(attrs={'class': 'border-3 border-gray-700 p-2 rounded-lg w-full'}),
        }