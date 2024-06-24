from django.db import models

class BookManager(models.Manager):
    def create_book(self, title):
        book = self.crete(title=title)
        return book

class Book(models.Model):
    title = models.CharField(max_length=25)
    objects = BookManager()

book = Book.objects.create_book("Python")
