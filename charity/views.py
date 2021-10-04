from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from NGO import models as NMODEL
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from NGO import forms as NFORM
from Donor.models import Feed


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'home.html')



def is_NGO(user):
    return user.groups.filter(name='NGO').exists()

def is_donor(user):
    return user.groups.filter(name='DONOR').exists()

def afterlogin_view(request):
    if is_donor(request.user):      
        return redirect('Donor/Donor-dashboard')
                
    elif is_NGO(request.user):
        accountapproval=NMODEL.NGO.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('NGO/NGO-dashboard')
        else:
            return render(request,'NGO_wait_for_approval.html')
    else:
        return redirect('admin-dashboard')


@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    return render(request,'admin_dashboard.html')


@login_required(login_url='adminlogin')
def admin_NGO_view(request):
    dict={
    'total_NGO':NMODEL.NGO.objects.all().filter(status=True).count(),
    'pending_NGO':NMODEL.NGO.objects.all().filter(status=False).count(),
    }
    return render(request,'admin_NGO.html',context=dict)


@login_required(login_url='adminlogin')
def admin_view_NGO_view(request):
    NGOs= NMODEL.NGO.objects.all().filter(status=True)
    return render(request,'admin_view_NGO.html',{'NGO':NGOs})



@login_required(login_url='adminlogin')
def admin_view_pending_NGO_view(request):
    NGOs= NMODEL.NGO.objects.all().filter(status=False)
    return render(request,'admin_view_pending_NGO.html',{'NGO':NGOs})




@login_required(login_url='adminlogin')
def approve_NGO_view(request,pk):
    NGO=NMODEL.NGO.objects.get(id=pk)
    NGO.status=True
    NGO.save()
    return HttpResponseRedirect('/admin-view-pending-NGO')
    

@login_required(login_url='adminlogin')
def reject_NGO_view(request,pk):
    NGO=NMODEL.NGO.objects.get(id=pk)
    user=User.objects.get(id=NGO.user_id)
    user.delete()
    NGO.delete()
    return HttpResponseRedirect('/admin-view-pending-NGO')



@login_required(login_url='adminlogin')
def update_NGO_view(request,pk):
    NGO=NMODEL.NGO.objects.get(id=pk)
    user=NMODEL.User.objects.get(id=NGO.user_id)
    userForm=NFORM.NGOUserForm(instance=user)
    NGOForm=NFORM.NGOForm(request.FILES,instance=NGO)
    mydict={'userForm':userForm,'NGOForm':NGOForm}
    if request.method=='POST':
        userForm=NFORM.NGOUserForm(request.POST,instance=user)
        NGOForm=NFORM.NGOForm(request.POST,request.FILES,instance=NGO)
        if userForm.is_valid() and NGOForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            NGOForm.save()
            return redirect('admin-view-NGO')
    return render(request,'update_NGO.html',context=mydict)



@login_required(login_url='adminlogin')
def delete_NGO_view(request,pk):
    NGO=NMODEL.NGO.objects.get(id=pk)
    user=User.objects.get(id=NGO.user_id)
    user.delete()
    NGO.delete()
    return HttpResponseRedirect('/admin-view-NGO')

def Reg_Login(request):
    return render(request,'Reg_Login.html')


@login_required(login_url='adminlogin')
def viewfeed(request):
    feeds= Feed.objects.all()
    return render(request,'admin_viewfeed.html',{'feedbacks':feeds})