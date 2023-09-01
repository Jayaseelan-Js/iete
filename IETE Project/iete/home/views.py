from django.shortcuts import render, HttpResponse
from .models import News, Publication, Events, Education, Research, Job, GalleryImage

# Create your views here.

def home(request):
    news = News.objects.get(id=1)
    context = {'news':news}
    return render(request, 'home.html', context)

def news(request):
    articles = News.objects.all()
    context = {'articles':articles}
    return render(request, 'news.html', context)

def news_detail(request, pk):
    news = News.objects.get(id=pk)
    return render(request, 'news_land.html', {'news':news})

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
    gallery = GalleryImage.objects.all()
    return render(request, 'galleries.html', {'gallery':gallery})

def about(request):
    return render(request, 'about1.html')

def membership(request):
    return render(request, 'membership.html')

def jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs1.html', {'jobs':jobs})

def research(request):
    research = Research.objects.all()
    return render(request, 'research.html', {'research':research})

def modeltest(request):
    article = News.objects.all()
    context = {'article': article}
    return render(request, 'about.html', context)