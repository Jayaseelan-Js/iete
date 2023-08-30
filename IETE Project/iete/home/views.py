from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def news(request):
    return render(request, 'news.html')

def event(request):
    return render(request, 'event.html')

def education(request):
    return render(request, 'education.html')

def publications(request):
    return render(request, 'publications.html')

def  galleries(request):
    return render(request, 'galleries.html')

def about(request):
    return render(request, 'about1.html')

def membership(request):
    return render(request, 'membership.html')