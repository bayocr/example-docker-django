from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
    def count_books(self):
        return Book.objects.filter(author=self).count()
    
    class Meta:
        ordering = ['id']


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    page_number = models.IntegerField()
    published_at = models.DateField()
    isbn_10 = models.CharField(max_length=20, unique=True)
    isbn_13 = models.CharField(max_length=20,unique=True)

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']