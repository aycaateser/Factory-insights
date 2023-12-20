from django.db import models

class Factory(models.Model):
    objects = models.Manager
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    product = models.CharField(max_length=100)
    employees = models.ManyToManyField("myapp.CustomUser")
    machines = models.ManyToManyField("myapp.Machine", blank=True, null=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name