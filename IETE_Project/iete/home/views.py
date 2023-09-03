from django.shortcuts import render, HttpResponse, redirect
from .models import News, Publication, Events, Education, Research, Job, GalleryImage
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import NewsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

def home(request):
    news = News.objects.get(id=1)
    context = {'news':news}
    return render(request, 'home.html', context)

def news(request):
    articles = News.objects.all()
    context = {'articles':articles}
    return render(request, 'news.html', context)

@login_required
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to create a new News object
            news = form.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()

    return render(request, 'create_news.html', {'form': form})

def news_land(request, pk):
    news = News.objects.get(id=pk)
    next_news = News.objects.filter(pk__gt=pk).order_by('pk').first()
    return render(request, 'news_land.html', {'news':news, 'next_news':next_news})

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

def admin_login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None and user.is_staff:
            auth_login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Credentials values are Inavlid')
            return redirect('login')

    else:
        return render(request, 'login.html')

@login_required()
def admin_logout(request):
    logout(request)
    return redirect('login')