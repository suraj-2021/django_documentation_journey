from django.db import models
import datetime

class Party(models.Model):
    name = models.CharField(max_length=40)
    birth_date = models.DateField()

    def invitednotinvited(self):
        if self.birth_date < datetime.date(2005, 1, 1):
            return f"Sorry to say but due to our policies {self.name} will not be invited to our party!"
        else:
            return f"Hi {self.name}, you're invited!"

    @property
    def nameanddate(self):
        return f"{self.name} was born on {self.birth_date}"
