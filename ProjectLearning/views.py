from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import User, Person,Lecture, Forum, Reply
from .forms import ForumForm, ReplyForm

def home(request):
    person = Person.objects.filter(user=request.user)
    context = {"person": person}
    return render(request, 'home.html', context)

def programs(request):
    person = Person.objects.filter(user=request.user)
    context = {"person": person}
    return render(request, 'programs.html', context)

def lectures(request):
    lecture = Lecture.objects.all().order_by('name').values()
    user = User.objects.filter(username=request.user.username).all()
    person = Person.objects.filter(user=request.user)
    context = {'lecture': lecture, 'user': user, "person": person}
    return render(request, 'lectures.html', context)

def test(request):
    person = Person.objects.filter(user=request.user)
    context = {"person": person}
    return render(request, 'test.html', context)

def answers(request):
    person = Person.objects.filter(user=request.user)
    context = {"person": person}
    return render(request, 'answers.html', context)

def profile(request):
    person = Person.objects.filter(user = request.user)
    context = {"person": person}
    return render(request, "profile.html", context)

def forum(request):
    person = Person.objects.filter(user=request.user)
    forum = Forum.objects.all()
    context = {"person": person, "forum": forum}
    return render(request, 'forum.html', context)

def replies(request):
    person = Person.objects.filter(user=request.user)
    replies = Reply.objects.all()
    context = {"person": person,"replies": replies}
    return render(request, 'replies.html', context)

def replyForum(request):
    person = Person.objects.filter(user=request.user)
    if(request.method == "POST"):
        form = ReplyForm(request.POST)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("replies")
    context = {"person": person,"form":ReplyForm}
    return render(request, "reply.html", context=context)

def addForum(request):
    person = Person.objects.filter(user=request.user)
    if(request.method == "POST"):
        form = ForumForm(request.POST)
        if(form.is_valid()):
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("forum")
    context = {"person": person, "form": ForumForm}
    return render(request, "addForum.html", context=context)

def contact(request):
    person = Person.objects.filter(user=request.user)
    context = {"person": person}
    return render(request, 'contact.html', context)
