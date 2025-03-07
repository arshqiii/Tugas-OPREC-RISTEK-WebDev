# quiz/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tryout, Question
from .forms import TryoutForm, QuestionForm

def show_main(req):
    tryout = Tryout.objects.all()
    context = {
        'list_tryout' : tryout
    }
    return render(req, "mainPage/index.html", context)
