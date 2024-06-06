from django.db import models

# Create your models here.
class StData(models.Model):
    St_id = models.IntegerField()
    Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=50)
    Maths = models.IntegerField()
    English = models.IntegerField
    Marks = models.IntegerField
    Grade = models.CharField(max_length=2)