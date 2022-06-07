from django.shortcuts import render, redirect, get_object_or_404

from inbox.models import Notification
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
        return redirect('home')
    form = PostForm()
    context = {
        "form": form,
    }
    return render(request, "posts/create_post.html", context=context)


def like_post(request, post_id):
    current_user_profile = UserProfile.objects.filter(user=request.user).first()
    post = Post.objects.filter(pk=post_id).first()
    liking_user_profile = UserProfile.objects.filter(user_id=request.user.id).first()
    is_liked_already = PostLikes.objects.filter(post=post, user=liking_user_profile).first()
    if is_liked_already:
        is_liked_already.delete()
        return redirect(request.META.get('HTTP_REFERER', 'home')+f"#{post.id}")
    post_like = PostLikes(user=liking_user_profile, post=post)
    post_like.save()
    notification = Notification.objects.create(
        notification_type=1,
        from_user=current_user_profile,
        to_user=post.owner,
        post=post
    )
    return redirect(request.META.get('HTTP_REFERER', 'home')+f"#{post.id}")


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
        notification = Notification.objects.create(
            notification_type=2,
            from_user=current_user_profile,
            to_user=post.owner,
            post=post
        )
    return redirect('single_post', post_id)


def edit_post(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated!')
            return redirect('edit_profile')
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(instance=post)
    context = {
        "form": form,
        "post": post,
    }
    return render(request, "posts/edit_post.html", context)


def delete_post(request, post_id):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    post = get_object_or_404(Post, pk=post_id)
    if post:
        post.delete()
    return redirect('user_profile', userprofile.user.username_slug)

