from django.urls import path
from Donor import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('Donorlogin', LoginView.as_view(template_name='Donorlogin.html'),name='Donorlogin'),
path('Donorsignup', views.Donor_signup_view,name='Donorsignup'),
path('Donor-dashboard', views.Donor_dashboard_view,name='Donor-dashboard'),
path('allreq', views.allreq,name='allreq'), 
path('feedback', views.feedback,name='feedback'), 
path('donate', views.donate,name='donate'), 
path('viewdonation', views.viewdonation,name='viewdonation'), 
]