from django.urls import path
from . import views
urlpatterns = [
 
    path('',views.signup),
    path('save_data',views.save_data,name="save_data"),

]