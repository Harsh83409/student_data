from django.urls import path
from . import views
urlpatterns = [
 
    path('',views.login),
    path('login2',views.login2,name='login2'),

]