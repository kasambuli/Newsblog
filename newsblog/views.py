from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfile,EditUserForm,CommentsForm,NewsForm
from .models import Profile,Comments,News,User
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.db import transaction
from newsapi import NewsApiClient
import requests

# Create your views here.


def index(request):
    '''
    function to diplay all news articles
    '''
    comments = Comments.objects.all()
    articles = News.objects.all()

    context = {
            "comments":comments,
            "articles": articles,

        }
    return render(request,'index.html',context)

@login_required(login_url='/accounts/login/')
def edit_profile(request,id):
    '''
    function to edit the user profile
    '''
    current_user = request.user
    profile = Profile.objects.get(user = current_user.id)
    if request.method == 'POST':
        profile_form = EditProfile(request.POST, request.FILES, instance=current_user.profile)
        user_form = EditUserForm(request.POST, instance=current_user)
        if profile_form.is_valid() and user_form.is_valid():
            profile = profile_form.save(commit=False)
            user = user_form.save(commit=False)
            profile.user = current_user
            profile.save()
            user.save()

            return redirect('/')
    else:
        profile_form = EditProfile()
        user_form = EditUserForm()
    context = {
        "current_user": current_user,
        "profile_form": profile_form,
        "user_form": user_form,
        "profile": profile,
        }
    return render(request, 'profile_form.html', context)

@login_required(login_url='/accounts/register/')
def news(request):
    '''
    function to create a news article
    '''
    current_user = request.user
    try:
        if request.method == 'POST':
            news_form = NewsForm(request.POST, request.FILES)
            if news_form.is_valid():
                news = news_form.save(commit=False)
                news.user = current_user
                news.save()
              

                return redirect('/')
        else:
            news_form = NewsForm()
            
        context = {
            "current_user": current_user,
            "news_form": news_form,

        }
    except ValueError:
        Http404  
    return render(request, 'news_form.html', context)

def comment(request,article_id):
    '''
    function to create a comment
    '''
    current_user = request.user
    current_article = News.objects.get(id = article_id)
    try:
        if request.method == 'POST':
            comment_form = CommentsForm(request.POST, request.FILES)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = current_user
                comment.save()
          

                return redirect('/')
        else:
            comment_form = CommentsForm()
            
        context = {
            "current_user": current_user,
            "comment_form": comment_form,
            "current_article":current_article,
            id: article_id,

        }
    except ValueError:
        Http404  
    return render(request, 'comment_form.html', context)
