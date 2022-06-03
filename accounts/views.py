from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, UserSignUpForm
from accounts.models import Account, UserProfile
from django.contrib import messages, auth
from posts.models import Post
from followers.models import UserFollowing
from django.contrib.auth.models import AnonymousUser


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
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

            profile = UserProfile()
            profile.user = user
            profile.profile_picture = "userprofile/default_user.png"
            profile.save()
            messages.error(request, "User successfully created.")
            return redirect('login')
        else:
            messages.error(request, "User with this username already exist.")
            return redirect('signup')

    form = UserSignUpForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context=context)


@login_required(login_url='login')
def home(request):
    posts = Post.objects.order_by("-created_at").all()
    context = {
        "posts": posts
    }
    return render(request, "home/home.html", context)


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, "You are logged out successfully.")
    return redirect('login')


@login_required(login_url='login')
def profile_page(request, username_slug):
    if request.method == "POST":
        current_user = request.user
        current_user_profile = UserProfile.objects.filter(user__username=current_user.username).first()
        user_to_follow = UserProfile.objects.filter(user__username_slug=username_slug).first()
        if current_user_profile.user.username != user_to_follow.user.username:
            user_follow = UserFollowing(followed_by=current_user_profile, followed_to=user_to_follow)
            user_follow.save()
            return redirect('user_profile', username_slug)
        else:
            messages.warning(request, "You can not follow this profile.")
            return redirect('user_profile', username_slug)
    current_user = request.user
    user_profile = get_object_or_404(UserProfile, user__username_slug=username_slug)
    current_user_profile_to_check = UserProfile.objects.filter(user__username=current_user.username).first()
    is_followed_by_current = UserFollowing.objects.filter(followed_by=current_user_profile_to_check,
                                                          followed_to=user_profile).first()
    user_posts = Post.objects.filter(owner__user=user_profile.user).order_by("created_at").all()
    context = {
        "user_profile": user_profile,
        "posts": user_posts,
        "is_followed": is_followed_by_current,
    }
    return render(request, "accounts/profile_page.html", context)


@login_required(login_url='login')
def unfollow(request, user_id):
    user = request.user
    followed_by = UserProfile.objects.filter(user=user).first()
    followed_to = UserProfile.objects.filter(user_id=user_id).first()
    find_user_to_unfollow = UserFollowing.objects.filter(followed_by=followed_by, followed_to=followed_to).first()
    find_user_to_unfollow.delete()
    return redirect("user_profile", followed_to.user.username_slug)


@login_required(login_url='login')
def search(request):
    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            users = UserProfile.objects.filter(user__username__icontains=keyword).all()
            context = {
                "users": users,
            }
            return render(request, "home/home.html", context)
    posts = Post.objects.order_by("-created_at").all()
    context = {
        "posts": posts
    }
    return render(request, "home/home.html", context)


def home_friends(request):
    return render(request, "home/home_followed_only.html")