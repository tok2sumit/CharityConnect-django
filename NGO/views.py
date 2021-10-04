from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Requirements
from django.forms.widgets import DateTimeBaseInput
from NGO.models import Contact
# Create your views here.

def NGO_signup(request):
    userForm=forms.NGOUserForm()
    NGOForm=forms.NGOForm()
    mydict={'userForm':userForm,'NGOForm':NGOForm}
    if request.method == 'POST':
        userForm=forms.NGOUserForm(request.POST)
        NGOForm=forms.NGOForm(request.POST,request.FILES)
        if userForm.is_valid() and NGOForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            NGO=NGOForm.save(commit=False)
            NGO.user=user
            NGO.save()
            my_NGO_group = Group.objects.get_or_create(name='NGO')
            my_NGO_group[0].user_set.add(user)
        return HttpResponseRedirect('ngologin')
        

    return render(request,'NGOsignup.html',mydict)


def is_NGO(user):
    return user.groups.filter(name='NGO').exists()

@login_required(login_url='ngologin')
@user_passes_test(is_NGO)
def NGO_dashboard_view(request):
    return render(request,'NGO_dashboard.html')

@login_required(login_url='ngologin')
@user_passes_test(is_NGO)
def pushreq(request):
    if request.method=="POST":
        nid= request.user.id
        ename= request.POST['ename']
        edesc= request.POST['edesc']
        edate= request.POST['edate']
        ereq = request.POST['ereq']

        req= Requirements.objects.create(nid=nid,ename=ename,edate=edate,edescription=edesc,ereq=ereq)
        req.save()
    
    return render(request,'NGO_Requirements.html')



@login_required(login_url='ngologin')
@user_passes_test(is_NGO)
def viewreq(request):
    nid= request.user.id
    reqs=Requirements.objects.filter(nid=nid)
    return render(request,'NGO_VRequirements.html',{'requests':reqs})


def Contactus(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phoneno = request.POST.get('phoneno')
        email = request.POST.get('email')
        querry = request.POST.get('querry')
        contact = Contact.objects.create(firstname=firstname,lastname=lastname,phoneno=phoneno,email=email,querry=querry,date=DateTimeBaseInput.today())
        contact.save()
    return render(request,'Contactus.html')
    #return HttpResponse("this is contact us page")