from django.db import models
from django.forms.models import model_to_dict
import pickle

class Club(models.Model):
    name = models.CharField(max_length=100)
    establishment_year = models.DateField()
    revenue = models.IntegerField()

    class Meta:
        verbose_name_plural = "Clubs"

    def __str__(self):
        return f"This club's name is {self.name}, it was established in year {self.establishment_year} and it generates {self.revenue} rupees per year"


club_1 = Club.objects.first()


my_dict = model_to_dict(club_1, fields=['name', 'establishment_year', 'revenue'])


my_pickle = pickle.dumps(my_dict)


new_instance = Club(**pickle.loads(my_pickle))
new_instance.save()
