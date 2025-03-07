from django.forms import ModelForm
from main.models import Tryout, Question

class TryoutForm(ModelForm):
    class Meta :
        model = Tryout
        fields = ['title', 'description']

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['tryout', 'text', 'answer']