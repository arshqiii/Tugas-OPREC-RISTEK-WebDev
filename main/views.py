# quiz/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Tryout, Question
from .forms import TryoutForm, QuestionForm

def show_main(req):
    tryout = Tryout.objects.all()
    context = {
        'list_tryout' : tryout
    }
    return render(req, "mainPage/index.html", context)

def tryout_create(req):
    if req.method == "POST":
        form = TryoutForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('tryout_list')
    else:
        form = TryoutForm()
    context = {'form': form}
    return render(req, 'addTryout/index.html', context) 

def tryout_edit(req, id):
    tryout = Tryout.objects.get(pk=id)
    form = TryoutForm(req.POST, instance=tryout)
    if req.method == 'POST' and form.is_valid() :
        form.save()
        return HttpResponseRedirect(reverse('main:tryout_detail'))
    
    context = {'form': form}
    return render(req, 'editTryout/index.html', context)

def tryout_delete(req,id):
    tryout = Tryout.objects.get(pk=id)
    tryout.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def tryout_detail(req, id):
    pass