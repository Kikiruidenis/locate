from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from HackOkapp.models import Lost 

def about(request):
    return render(request,"about.html")

def home(request):
    lost = Lost.objects.filter(found=True)[:2] #retrivies top 3
    return render(request, "index.html",{'lost':lost})

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
