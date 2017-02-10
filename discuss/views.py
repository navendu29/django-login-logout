from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.http import Http404

from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm,LoginForm
from.models import Register
from django.http import HttpResponse

from .models import Register
# Create your views here.

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        uname = form.cleaned_data['name']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']

        x=Register.objects.get_or_create(name=uname)
        r=Register.objects.all()
        user = authenticate(name=uname, password=password)
        return render(request, 'discuss/login.html',{'r':r})

    form = UserForm()
    context = {
            "form": form,
    }
    return render(request, 'discuss/register.html', context)


def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        uname = form.cleaned_data['name']
        password = form.cleaned_data['password']

        try:
           x=Register.objects.get(name=uname,password=password)
        except Register.DoesNotExist:
            return HttpResponse("does not exists")
        r = Register.objects.all()
        return HttpResponse("logged in"+x.name)
        #return render(request, 'discuss/login.html',{'r':r})
    return render(request, 'discuss/register.html',{'form':form})




