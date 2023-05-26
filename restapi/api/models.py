from django.db import models

class Student(models.Model):
    name=models.CharField( max_length=50)
    rollno=models.IntegerField()
    classs=models.CharField(max_length=50)
    section=models.CharField(max_length=50)
    mobile=models.IntegerField()
    def __str__(self) -> str:
        return self.name