from django.shortcuts import render
from signup.models import SignUpData 

def get_data(request, studentid):
    user_data = SignUpData.objects.get(St_id = studentid)
    context = {'data': user_data}
    print(context)
    return render(request, 'studentData/data.html', context)
