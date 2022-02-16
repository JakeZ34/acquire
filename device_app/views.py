from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

'''from django.shortcuts import render, redirect
from .models import *
import bcrypt
import re
from django.contrib import messages
#from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        return redirect('/main')


def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/main')


#def profile(request):
    #user = User.objects.get(id=request.session['user_id'])
    #context = {
    #"user": User.objects.get(id=request.session['user_id'])
    #}
    #return render(request, "profile.html", context)


def main_page(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'posts': Post.objects.all()
    }
    return render(request, 'main.html', context)


def make_post(request):
    if(request.method == "POST"):
        errors = Post.objects.post_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/main')
        else:
            post = Post.objects.create(
                message=request.POST['mess'],
                title=request.POST['title'],
                description=request.POST['description'],
                poster=User.objects.get(id=request.session['user_id'])
            )
    return redirect('/main')


def add_like(request, id):
    liked_message = Post.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['user_id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/main')


def logout(request):
    request.session.clear()
    return redirect('/')

#@login_required


def edit(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'posts': Post.objects.filter(id=id)
    }
    return render(request, 'updatepost.html', context)


def update(request, id):
    errors = Post.objects.post_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return render(request, 'updatepost.html')
    else:
        post = Post.objects.get(id=id)
        post.message = request.POST['mess']
        post.title = request.POST['title']
        post.description = request.POST['description']
        poster = User.objects.get(id=request.session['user_id'])
        post.save()
    return redirect('/main')


def delete(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('/main')


def back(request):
    return redirect('/main')


def show_post(request, id):
    id = id
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'posts': Post.objects.filter(id=id)
    }
    return render(request, 'showpost.html', context)


def welcome(request):
    return render(request, 'loginpage.html')


#def show_post(request, id):
    #context = {
        #'post': Post.objects.get(id=id)
    #}
    #return render(request, 'showpost.html', context)
'''