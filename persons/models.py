from django.db import models
    

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if not isinstance(self.first_name, str) or not isinstance(self.last_name, str):
            raise ValueError("First name and last name must be strings.")
            print("Please input a string for first_name and last_name.")

