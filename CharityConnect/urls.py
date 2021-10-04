"""CharityConnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from charity import views
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name=''),
    path('logout', LogoutView.as_view(template_name='home.html'),name='logout'),
    path('NGO/',include('NGO.urls')),
    path('Donor/',include('Donor.urls')),
    path('Reg_Login', views.Reg_Login,name='Reg_Login'),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    
    path('admin-NGO', views.admin_NGO_view,name='admin-NGO'),
    path('admin-view-pending-NGO', views.admin_view_pending_NGO_view,name='admin-view-pending-NGO'),
    path('admin-view-NGO', views.admin_view_NGO_view,name='admin-view-NGO'),
    path('approve-NGO/<int:pk>', views.approve_NGO_view,name='approve-NGO'),
    path('reject-NGO/<int:pk>', views.reject_NGO_view,name='reject-NGO'),
    path('update-NGO/<int:pk>', views.update_NGO_view,name='update-NGO'),
    path('delete-NGO/<int:pk>', views.delete_NGO_view,name='delete-NGO'),

     path('viewfeed', views.viewfeed,name='viewfeed'),
]
