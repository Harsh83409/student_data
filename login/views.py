from django.shortcuts import render
from django.contrib.auth.models import auth
from signup import models
from studentData.views import get_data
# Create your views here.

def login(request):
   return render(request,'login/login.html')



def login2(request):
   if request.method == 'POST':
    studentid = request.POST['studentId']
    password = request.POST['password']
    if (models.SignUpData.objects.filter(St_id=studentid).exists() and  models.SignUpData.objects.filter(password=password).exists()):
      print("hi")
      return get_data(request, studentid)
    return render (request,'login/login.html')