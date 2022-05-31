from django.shortcuts import render
from .forms import PostForm


# Create your views here.
def create_post(request):
    form = PostForm()
    context = {
        "form": form,
    }
    return render(request, "posts/create_post.html", context=context)
