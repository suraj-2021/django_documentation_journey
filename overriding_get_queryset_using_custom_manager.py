from django.db import models

class BookManager(models.Manager):
      def get_queryset(self):
          queryset = super().get_queryset()
          return queryset.exclude(book_label=None).exclude(book_label__iexact=" ")


class Book(models.Model):
      title = models.CharField(max_length=50)
      original_publication_date= models.IntegerField()
      book_label = models.CharField(blank=True, null = True)
      objects = BookManager()


      def __str__(self):
          return self.title
