from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post, PostLikes
from accounts.models import UserProfile


# Create your views here.
def create_post(request):
    if request.method == "POST":
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()
        photo = request.FILES.get('photo')
        description = request.POST["description"]
        post = Post(owner=user_profile, photo=photo, description=description)
        post.save()
    form = PostForm()
    context = {
        "form": form,
    }
    return render(request, "posts/create_post.html", context=context)


def like_post(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    liking_user_profile = UserProfile.objects.filter(user_id=request.user.id).first()
    post_like = PostLikes(user=liking_user_profile, post=post)
    post_like.save()
    return redirect('home')