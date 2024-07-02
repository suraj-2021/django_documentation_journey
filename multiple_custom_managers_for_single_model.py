class QueManager (models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(effectiveness="1")

class CravingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(effectiveness="1")

class ResponseManager(models.Manager):
     def get_queryset(self)
         return super().get_queryset().filter(effectiveness="1")

class RewardManager(models.Manager):
     def get-queryset(self):
         return super().get_queryset().filter(effectiveness="1")


class Habits(models.Model):
    ques =  models.CharField(max_length=1, choices={"1": _("5-stars"), "2": _("4-stars","3":_("3-stars"),"4":_("2-stars"), "5":_("1-star")})
    craving = models.CharField(max_length=1, choices={"1": _("5-stars"), "2": _("4-stars","3":_("3-stars"),"4":_("2-stars"), "5":_("1-star")})
    response = models.CharField(max_length=1, choices={"1": _("5-stars"), "2": _("4-stars","3":_("3-stars"),"4":_("2-stars"), "5":_("1-star")})
    Reward = models.CharField(max_length=1, choices={"1": _("5-stars"), "2": _("4-stars","3":_("3-stars"),"4":_("2-stars"), "5":_("1-star")})

    objects = models.Manager()
    ques = QueManager()
    cravings = CravingManager()
    responses  = ResponseManager()
    rewards = RewardManager()
