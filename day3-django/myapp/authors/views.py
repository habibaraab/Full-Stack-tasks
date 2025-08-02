from django.shortcuts import render
from .models import Book, Author
from django.shortcuts import render, get_object_or_404


def all_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'authors/all_books.html', context)

def all_authors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'authors/all_authors.html', context)


def author_books(request, author_id):
    
    author = get_object_or_404(Author, pk=author_id)

    books = Book.objects.filter(author=author)
    
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'authors/author_books.html', context)
