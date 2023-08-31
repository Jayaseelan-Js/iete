from django.shortcuts import render, HttpResponse
from .models import News, Publication, Events, Education

# Create your views here.

def home(request):
    return render(request, 'home.html')

def news(request):
    articles = News.objects.all()
    context = {'articles':articles}
    return render(request, 'news.html', context)

def event(request):
    event = Events.objects.all()
    context = {'events':event}
    return render(request, 'event.html', context)

def education(request):
    edu = Education.objects.all()
    context = {'education':edu}
    return render(request, 'education.html', context)

def publications(request):
    publication = Publication.objects.all()
    context = {'publication':publication}
    return render(request, 'publications.html', context)

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