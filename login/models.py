from django.db import models

# Create your models here.
class StudentLogin(models.Model):
    st_id = models.IntegerField('primary_key=True')
    st_password = models.CharField(max_length=15)
    

    # def __str__(self):
    #     return (self.st_id )
    