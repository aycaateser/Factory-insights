from django.db import models

class Machine(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.name}"