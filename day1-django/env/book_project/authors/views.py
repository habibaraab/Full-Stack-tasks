from django.shortcuts import render

def home(request):
    return render(request, 'authors/home.html')

def about(request):
    return render(request, 'authors/about.html')

def contact(request):
    return render(request, 'authors/contact.html')