from django.db import models

class Person(models.Model):
    SHIRT_CHOICES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
    }
    name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_CHOICES)

x = Person(name="Great", shirt_size="L")
display_size = x.get_shirt_size_display()

print(f"The shirt size for the person {x.name} is {display_size}")
