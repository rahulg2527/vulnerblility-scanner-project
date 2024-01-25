from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello")

def signUp(request):
    return render(request, "authentication/signUp.html")

def signIn(request):
    return render(request, "authentication/signIn.html")

def signout(request):
    pass
