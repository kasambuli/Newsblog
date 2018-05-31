from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    '''
    function to diplay all news articles
    '''
    return(render,'index.html')