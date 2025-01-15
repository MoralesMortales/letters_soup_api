from django.db import models
from django.contrib.postgres.fields import ArrayField

class User_app(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique = True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Soup(models.Model): 
    email = models.ForeignKey(User_app, on_delete=models.CASCADE)  
    row = models.PositiveIntegerField()  
    col = models.PositiveIntegerField()  
    soup = models.CharField(max_length=500) 
    words = ArrayField(models.CharField(max_length=500))

    def __str__(self):
        return f"Sopa de {self.email}"


