from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import UserForm, UserSignUpForm
from accounts.models import Account
from django.contrib import messages, auth


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("home")
        else:
            messages.error(request, "Invalid login credentials")
            return redirect("login")
    form = UserForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context=context)


def signup(request):
    if request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = form.cleaned_data["username"]
            check_if_user_exists = Account.objects.filter(username__iexact=username)
            if check_if_user_exists:
                messages.error(request, "User with this username already exist.")
                return redirect('signup')
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                               password=password, username=username)
            user.phone_number = phone_number
            user.username_slug = username
            user.save()
            messages.error(request, "User successfully created.")
            return redirect('login')
        else:
            messages.error(request, "User with this username already exist.")
            return redirect('signup')

            # create user profile
            # profile = UserProfile()
            # profile.user_id = user.id
            # profile.profile_picture = "default/default_user.png"
            # profile.save()
            # print(user.username)
    form = UserSignUpForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context=context)


def home(request):
    return render(request, "home/home.html")