from django.db import models

class ActiveUserStatus(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class User(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    objects = models.Manager() 
    active_users = ActiveUserStatus()

active_users = User.active_users.all()
