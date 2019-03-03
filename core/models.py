from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class Result(models.Model):
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    body_mass_index = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



