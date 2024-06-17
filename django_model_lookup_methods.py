from django.core.exceptions import ObjectDoesNotExist

try:
    desired_book = Book.objects.get(name__icontains="Health")
except ObjectDoesNotExist:
    desired_book = None
