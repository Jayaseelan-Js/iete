from django.shortcuts import render, HttpResponse
from .models import News

# Create your views here.

def home(request):
    return render(request, 'home.html')

def news(request):
    articles = News.objects.all()
    context = {'articles':articles}
    return render(request, 'news.html', context)

def event(request):
    return render(request, 'event.html')

def education(request):
    return render(request, 'education.html')

def publications(request):
    return render(request, 'publications.html')

def galleries(request):
    return render(request, 'galleries.html')

def about(request):
    return render(request, 'about1.html')

def membership(request):
    return render(request, 'membership.html')

def jobs(request):
    return render(request, 'jobs1.html')

def research(request):
    return render(request, 'research.html')

def modeltest(request):
    article = News.objects.all()
    context = {'article': article}
    return render(request, 'about.html', context)