from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
def home(request):
    return render(request,'home.html')

def registration(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf,'pf':pf}

    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            UFO=UFD.save(commit=False)
            password=UFD.cleaned_data['password']
            UFO.set_password(password)
            UFO.save()

            PFO=PFD.save(commit=False)
            PFO.profile_user=UFO
            PFO.save()

            send_mail('Registration','Registration is successfully','loga1831@gmail.com',[UFO.email],fail_silently=False)
            return HttpResponse('registration is succeffull')


    return render(request,'registration.html',d)