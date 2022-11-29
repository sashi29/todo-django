from django.db import models

# Create your models here.
class Todolist(models.Model): 
    name=models.CharField(max_length=60) 
    status=models.BooleanField(default=False) 

    def __str__(self): 
        return self.name 
        