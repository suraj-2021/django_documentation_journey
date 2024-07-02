
class TreeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(species="Peepal")



class Tree(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)

    objects = models.Manager()
    tree_objects = TreeManager()

