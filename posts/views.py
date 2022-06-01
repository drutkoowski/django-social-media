from django.shortcuts import render
from .forms import PostForm
from .models import Post
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
        print(description)
        print(photo)
    form = PostForm()
    context = {
        "form": form,
    }
    return render(request, "posts/create_post.html", context=context)
