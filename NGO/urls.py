from django.urls import path
from NGO import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('ngosignup', views.NGO_signup,name='ngosignup'),
path('ngologin', LoginView.as_view(template_name='NGOlogin.html'),name='ngologin'),
path('NGO-dashboard', views.NGO_dashboard_view,name='NGO-dashboard'),
path('pushreq', views.pushreq,name='pushreq'),
path('viewreq', views.viewreq,name='viewreq'),
path('Contactus', views.Contactus,name='Contactus'),
]