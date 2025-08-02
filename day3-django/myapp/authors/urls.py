from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.all_books, name='all_books'),
    path('authors/', views.all_authors, name='all_authors'),
    path('authors/<author_id>/', views.author_books, name='author_books'), 
]