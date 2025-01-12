from django.db import models

class User_app(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique = True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Word(models.Model): 
    length = models.IntegerField()  
    x = models.IntegerField()  
    y = models.IntegerField()  
    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word

class Soup(models.Model): 
    email = models.ForeignKey(User_app, on_delete=models.CASCADE)  
    row = models.PositiveIntegerField()  
    col = models.PositiveIntegerField()  
    letters = models.CharField(max_length=500) 
    words = models.ManyToManyField(Word)

    def __str__(self):
        return f"Sopa de {self.email}"
