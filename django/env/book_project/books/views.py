from django.shortcuts import render

def home(request):
    return render(request, 'books/home.html')

def about(request):
    return render(request, 'books/about.html')

def contact(request):
    return render(request, 'books/contact.html')