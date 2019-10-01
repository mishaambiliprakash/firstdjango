from django.db import models

# Create your models here.

gender_choices=(
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHERS')
)

class Students(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.CharField(max_length=10)
    course=models.CharField(max_length=50)
    address=models.TextField()
    gender=models.CharField(max_length=1,choices=gender_choices,default='M')

class Faculty(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=10)
    salary=models.CharField(max_length=50)   
    dept=models.CharField(max_length=50)