from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    roll_number = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
