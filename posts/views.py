from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, PostLikes, PostComments
from accounts.models import UserProfile
from django.contrib import messages


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
    is_liked_already = PostLikes.objects.filter(post=post, user=liking_user_profile).first()
    if is_liked_already:
        is_liked_already.delete()
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    post_like = PostLikes(user=liking_user_profile, post=post)
    post_like.save()
    return redirect(request.META.get('HTTP_REFERER', 'home'))


def single_post(request, post_id):
    form = CommentForm()
    post = Post.objects.filter(pk=post_id).first()
    current_user_profile = UserProfile.objects.filter(user_id=request.user.id).first()
    comments = PostComments.objects.filter(post=post).all()
    context = {
        "post": post,
        "user_profile": current_user_profile,
        "form": form,
        "comments": comments,
    }
    return render(request, "posts/single_post.html", context)


def add_comment(request, post_id):
    if request.method == "POST":
        post = Post.objects.filter(pk=post_id).first()
        current_user_profile = UserProfile.objects.filter(user_id=request.user.id).first()
        content = request.POST["content"]
        comment = PostComments(user=current_user_profile, post=post, content=content)
        comment.save()
    return redirect('single_post', post_id)