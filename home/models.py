from django.db import models

# Create your models here.


class Receiver(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    city = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.name + "\t" + self.city
