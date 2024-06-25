from django.db import models

class Cheese(models.Model):
      name = models.CharField(max-length=50)
      price = models.IntegerField()
      sold = models.IntegerField()

    class Meta:
          verbose_name_plural = "Cheeses"

    def __str__(self):
        return self.name


sunday_cheese = Cheese.objects.get(name="Italian")\


sunday_cheese.price +=1
sunday_chaeese.save()


monday_cheese = Cheese.objects.get(name="Frencgh Cheese")
monday_cheese.sold = F("sold")+1

june = Cheese.objects.flter(name="Algerian Cheese")
june.name = "Egyptian Chesee"
june.save(upadate_fields=["name"])



