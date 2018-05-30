from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    function to diplay all news articles
    '''
    return(render,'index.html')