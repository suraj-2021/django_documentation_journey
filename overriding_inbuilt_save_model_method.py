from django.db import models

class Notebook(models.Model):
      name = models.CharField(max_length=20)
      tagline = models.TextField()

    def save(self,*args,**kwargs):
        if self.name == "blue Sea":
          return #sorry you can't label notebooks with the name provided
        else:
          super().save(*args,**kwargs)


