from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

books = Book.objects.filter(
    title__icontains='python',
    publication_date__year__gte=2020,
    price__lt=50.00
)
