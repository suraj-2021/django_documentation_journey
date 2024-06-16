from django.db import models

class MiningAsteroids(models.Model):
    rocket = models.CharField(max_length=130)
    cost = models.IntegerField()

    def is_expensive(self):
        return self.cost > 5000000

    @property
    def name(self):
        return f"{self.rocket}"
