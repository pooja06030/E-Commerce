from django.db import models


class Custmore(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_name = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)