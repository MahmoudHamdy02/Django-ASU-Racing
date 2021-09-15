from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    age = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.age}, {self.email}, {self.gender}"