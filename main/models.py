from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    position = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    image = models.ImageField(upload_to='image', blank=True)

    def __str__(self):
        return f"{self.name } {self.position}"

class Hello(models.Model):
    name = models.CharField(max_length=20)