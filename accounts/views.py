from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, UserSignUpForm


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
    form = UserForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context=context)


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
    form = UserSignUpForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context=context)