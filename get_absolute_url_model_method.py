# models.py
from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=100)
    # Add other fields as needed

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})
