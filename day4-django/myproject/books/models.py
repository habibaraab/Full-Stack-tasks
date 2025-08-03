# books/models.py
from django.db import models
from django.urls import reverse

class Book(models.Model):
    """Represents a book in the database."""

    # --- Choices for the book type field ---
    BOOK_TYPE_CHOICES = (
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science', 'Science'),
        ('History', 'History'),
    )

    # --- Model Fields ---
    name = models.CharField(max_length=200, verbose_name="Book Name")
    book_type = models.CharField(
        max_length=20,
        choices=BOOK_TYPE_CHOICES,
        verbose_name="Book Type"
    )

    def __str__(self):
        """Returns the string representation of the model, which is the book's name."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a specific instance of the book."""
        # This URL is used to redirect the user after a book is created or updated.
        return reverse('book-detail', kwargs={'pk': self.pk})