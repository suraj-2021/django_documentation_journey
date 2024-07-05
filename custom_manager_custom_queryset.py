from django.db import models

class BlackQuery(models.QuerySet):
    def blue_revenue(self):
        return self.filter(blue_rose_revenue__gt=100000)

    def dragon_revenue(self):
        return self.filter(dragon_fly_revenue__gt=100000)

class BlackManager(models.Manager):
    def get_queryset(self):
        return BlackQuery(self.model, using=self._db)

class BlackRock(models.Model):
    audit_name = models.CharField(max_length=120)
    blue_rose_revenue = models.IntegerField()
    dragon_fly_revenue = models.IntegerField()
    objects = BlackManager()

black_rock_instance = BlackRock.objects.create(audit_name="Blue Ocean", blue_rose_revenue=120000, dragon_fly_revenue=95000)
x = BlackRock.objects.blue_revenue()
y = BlackRock.objects.dragon_revenue()
