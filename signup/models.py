from django.db import models
# models.py

# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

class SignUpData(models.Model):
   St_id = models.IntegerField()
   Name = models.CharField(max_length=20)
   email = models.EmailField(max_length=50)
   phone = models.IntegerField()
   dob = models.DateField()
   maths = models.IntegerField(default=0)
   english = models.IntegerField(default=0)
   grade = models.CharField(max_length=2,default='')
   gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
   address = models.TextField() 
   # Add new columns here
   password = models.CharField(max_length=128)
   confirm_password = models.CharField(max_length=128)


   def __str__(self):
      return f"student id: {self.St_id} and Email: {self.email}"












