from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request,'home.html');
    elif request.POST.get('movie_title',None):
        return redirect('get_search_result', request.POST.get('movie_title') )
        

def get_search_result(request,movie_title):
    from urllib.parse import quote
    url = 'http://www.btbtdy.com/search/'+movie_title+'.html'
    from .get_links import get_links
    download_urls = get_links.get_download_urls(url)
    return render(request,'download_links.html',context={
        'download_links':download_urls
    })