from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Tryout, Question
from .forms import TryoutForm, QuestionForm

#========================================================================
def show_main(req):
    tryout = Tryout.objects.all()
    context = {
        'list_tryout': tryout
    }
    return render(req, "mainPage/index.html", context)
#========================================================================
def tryout_create(req):
    if req.method == "POST":
        form = TryoutForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = TryoutForm()
    context = {'form': form}
    return render(req, 'addTryout/index.html', context)
#========================================================================
def tryout_edit(req, id):
    tryout = get_object_or_404(Tryout, pk=id)

    if req.method == 'POST':
        form = TryoutForm(req.POST, instance=tryout)
        if form.is_valid():
            form.save()
            return redirect('main:tryout_detail', id)

    else:
        form = TryoutForm(instance=tryout)

    context = {'form': form, 'tryout': tryout}
    return render(req, 'editTryout/index.html', context)
#========================================================================
def tryout_delete(req, id):
    tryout = get_object_or_404(Tryout, pk=id)
    tryout.delete()
    return redirect('main:show_main')
#========================================================================
def tryout_detail(req, id):
    tryout = get_object_or_404(Tryout, pk=id)
    questions = Question.objects.filter(tryout=tryout)
    
    context = {
        'tryout': tryout,
        'questions': questions,
    }
    return render(req, 'detailTryout/index.html', context)
#========================================================================
def question_create(req, tryout_id):
    tryout = get_object_or_404(Tryout, pk=tryout_id)
    
    if req.method == "POST":
        form = QuestionForm(req.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.tryout = tryout
            question.save()
            return redirect('main:tryout_detail', tryout.id)
    else :
        form = QuestionForm()
    
    context = {'form' : form, 'tryout':tryout}
    return render(req, "addQuestion/index.html", context)
#========================================================================
def question_edit(req, id):
    question = get_object_or_404(Question, pk=id)
    tryout = question.tryout
    
    if req.method == "POST":
        form = QuestionForm(req.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('main:tryout_detail', id=tryout.id)
    else :
        form = QuestionForm(instance=question)
    context = {'form' : form, 'question':question, 'tryout':tryout}
    return render(req, "editQuestion/index.html", context)
#========================================================================
def question_delete(req, id):
    question = get_object_or_404(Question, pk=id)
    tryout_id = question.tryout.id
    question.delete()
    return redirect('main:tryout_detail', tryout_id)
