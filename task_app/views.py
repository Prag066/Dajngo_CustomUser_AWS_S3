from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from .models import MyUser
from .forms import MyUserForm

def UserRegistration(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        
        print('r',request.FILES)
        profile_image = request.FILES['profile_image']
        # fs = FileSystemStorage()
        # filename = fs.save(profile_image.name,profile_image)
        # url = fs.url(filename)

        position = request.POST['position']
        location = request.POST['location']
        mobile = request.POST['mobile']
        password = request.POST['password']
        MyUser.objects.create_user(email=email,password=password,profile_image=profile_image,position=position,location=location,
            mobile=mobile,first_name=first_name,last_name=last_name)
        return redirect('/login/')
    context = {}
    return render(request,'task_app/registration.html',context)

# def UserRegistration(request):
#     if request.method == "POST" :
#         form = MyUserForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#     else:
#         form = MyUserForm()
#     context = {
#         'form':form
#     }
#     return render(request,'task_app/registration.html',context)

def UserLoggedIn(request):
    emails = [user.email for user in MyUser.objects.all()]
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if email not in emails:
            messages.error(request,'email is not registred')
        else:
            user = authenticate(request,email=email, password=password)
            if user is not None:
                login(request,user)
                return redirect('/user-profile')
            else:
                messages.warning(request,'UserName and Password does not match. Try again')
    context = {
    }
    return render(request,'task_app/login.html',context)

def UserProfile(request):
    # user_profile = MyUser.objects.all()
    context = {
        'user_profile':request.user
        }
    return render(request,'task_app/profile.html',context)


