from django.db import models


# Create your models here.
class Contacts(models.Model):
    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name
