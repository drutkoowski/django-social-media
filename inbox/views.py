from django.db.models import Q
from django.shortcuts import render, redirect
from accounts.models import UserProfile
from inbox.forms import MessageForm, ThreadForm
from inbox.models import ThreadModel, MessageModel
from django.contrib import messages


# Create your views here.


def inbox(request):
    user_profile = UserProfile.objects.get(user=request.user)
    threads = ThreadModel.objects.filter(Q(user=user_profile) | Q(receiver=user_profile))

    context = {
        "threads": threads,
        "userprofile": user_profile,
    }
    return render(request, "inbox/inbox.html", context)


def thread(request, pk):
    form = MessageForm()
    current_user_profile = UserProfile.objects.get(user=request.user)
    user_thread = ThreadModel.objects.get(pk=pk)
    message_list = MessageModel.objects.filter(thread__pk__contains=pk)
    context = {
        "thread": user_thread,
        "form": form,
        "message_list": message_list,
        "current_user_profile": current_user_profile,
    }
    return render(request, "inbox/thread.html", context)


def create_thread(request):
    current_user_profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = ThreadForm(request.POST)

        user = request.POST.get('username')
        requested_user_profile = UserProfile.objects.get(user=request.user)
        try:
            receiver = UserProfile.objects.get(user__username=user)
            if ThreadModel.objects.filter(user=requested_user_profile, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=requested_user_profile, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver, receiver=requested_user_profile).exists():
                thread = ThreadModel.objects.filter(user=receiver, receiver=requested_user_profile)[0]
                return redirect('thread', pk=thread.pk)
            if form.is_valid():
                thread = ThreadModel(user=requested_user_profile, receiver=receiver)
                thread.save()
                return redirect('thread', pk=thread.pk)
        except:
            messages.error(request, "Invalid username")
            return redirect('create-thread')
    form = ThreadForm()
    context = {
        "form": form,
        "user_profile": current_user_profile,
    }
    return render(request, "inbox/create_thread.html", context)


def create_message(request, pk):
    if request.method == "POST":
        requested_user_profile = UserProfile.objects.get(user=request.user)
        form = MessageForm(request.POST, request.FILES)
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == requested_user_profile:
            receiver = thread.user
        else:
            receiver = thread.receiver
        if form.is_valid():
            message = form.save(commit=False)
            message.thread = thread
            message.sender_user = requested_user_profile
            message.receiver_user = receiver
            message.save()

        # notification = Notification.objects.create(
        #     notification_type=4,
        #     from_user=request.user,
        #     to_user=receiver,
        #     thread=thread
        # )
        return redirect('thread', pk=pk)
