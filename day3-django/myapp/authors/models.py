from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField() 
    email = models.EmailField(unique=True) 
    gender = models.CharField(max_length=10) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200) 
    type = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books') 

    def __str__(self):
        return self.name