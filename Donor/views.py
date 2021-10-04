from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group
from . import forms
from django.contrib.auth.decorators import login_required,user_passes_test
from NGO.models import Requirements
from Donor.models import Donation, Feed
# Create your views here.

def Donor_signup_view(request):
    userForm=forms.DonorUserForm()
    DonorForm=forms.DonorForm()
    mydict={'userForm':userForm,'DonorForm':DonorForm}
    if request.method=='POST':
        userForm=forms.DonorUserForm(request.POST)
        DonorForm=forms.DonorForm(request.POST,request.FILES)
        if userForm.is_valid() and DonorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            Donor=DonorForm.save(commit=False)
            Donor.user=user
            Donor.save()
            my_Donor_group = Group.objects.get_or_create(name='DONOR')
            my_Donor_group[0].user_set.add(user)
        return HttpResponseRedirect('Donorlogin')
    return render(request,'Donorsignup.html',context=mydict)



def is_Donor(user):
    return user.groups.filter(name='DONOR').exists()

@login_required(login_url='Donorlogin')
@user_passes_test(is_Donor)
def Donor_dashboard_view(request):
    return render(request,'Donor_dashboard.html')


@login_required(login_url='Donorlogin')
@user_passes_test(is_Donor)
def allreq(request):
    reqs= Requirements.objects.all()
    return render(request,'Donor_AllRequirements.html',{'requests':reqs})






@login_required(login_url='Donorlogin')
@user_passes_test(is_Donor)
def feedback(request):
    if request.method=="POST":
        Name= request.user.first_name
        email= request.user.email
        feedback=request.POST['feedback']
        f= Feed.objects.create(Name=Name,email=email,feed=feedback)
        f.save()
        return redirect(Donor_dashboard_view)

    return render(request,'Donor_feedback.html')

@login_required(login_url='Donorlogin')
@user_passes_test(is_Donor)
def donate(request):

    if request.method=="POST":
        donation=int(request.POST['donate'])
        eid=int(request.GET.get('eid'))
        req=Requirements.objects.get(id=eid)
        amount= req.ereq - donation
        Requirements.objects.filter(id=eid).update(ereq=amount)
        id=request.user.id
        d=Donation.objects.create(donor_id=id,amount=donation,ename=req.ename)
        d.save()
        return redirect(allreq)
        
    
    id=request.GET.get('id')
    req= Requirements.objects.get(id=id)
    return render(request,'Donor_Donate.html',{'req':req})



@login_required(login_url='Donorlogin')
@user_passes_test(is_Donor)
def viewdonation(request):
    id=request.user.id
    reqs= Donation.objects.filter(donor_id=id)
    return render(request,'Donor_AllDonations.html',{'donations':reqs})
