from django.shortcuts import render
from login import *
from .models import SignUpData
# Create your views here.
def signup(request):
    print("hello")
    return render (request,'signup/signup.html')



def save_data(request):
    print("Save Data ")
    if request.method  == "POST":
        stuId = request.POST['studentId']
        studName =  request.POST['name']
        studEmail =  request.POST['email']
        studphn =  request.POST['phone']
        studdob =  request.POST['dob']
        studmarks1 =  request.POST['maths']
        studmarks2 =  request.POST['english']
        studgrade =  request.POST['grade']
        studTmarks =  request.POST['marks']
        studAddress =  request.POST['address'] 
        gender =  request.POST['gender']
        passwd = request.POST['password']
        com_passwd = request.POST['comfirm-password']  

        if passwd == com_passwd:
            if  SignUpData.objects.filter(St_id=stuId).exists():
                print("please check student id")
            elif SignUpData.objects.filter(email=studEmail).exists():
                print("please check student Email")
            else:
                user = SignUpData.objects.create(St_id = stuId,Name = studName,email = studEmail,phone=studphn,
                                                 dob=studdob,
                                                 maths = studmarks1,
                                                 english = studmarks2,
                                                 grade = studgrade,
                                                 gender = gender,
                                                 address = studAddress,
                                                 password= passwd,
                                                 confirm_password = com_passwd)
                
                user.save();
                print("save data")

        
        print(studgrade,studAddress,studdob,studmarks1,studEmail,studmarks2,studphn,studTmarks)
    return render(request,'login/login.html')