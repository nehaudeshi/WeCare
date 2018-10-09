from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Volunteer, Blog
# Create your views here.
def index(request):
    return render(request, 'WeCareApp/index.html')

def about(request):
    return render(request, 'WeCareApp/about.html')

def gethelp(request):
    return render(request, 'WeCareApp/gethelp.html')


def volunteer(request):
    return render(request, 'WeCareApp/volunteer.html')


def contact(request):
    return render(request, 'WeCareApp/contact.html')

def blogs(request):
    blogs = Blog.objects.filter()
    textss = list()
    headss = list()
    for i in blogs:
        textss.append(i.text)
        headss.append(i.heading)
    blogs_send = zip(headss,textss)
    return render(request, 'WeCareApp/blogs.html', {'blogs': blogs_send })

def newBlog(request):
    if request.method=='POST':
        blog = Blog.objects.create(
            heading = request.POST.get('heading'),
            text = request.POST.get('text')
            )
        return HttpResponseRedirect("/profile")

@login_required
def profile(request):
    current_user = request.user
    vol=None
    if Volunteer.objects.filter(id=current_user).exists():
        vol = Volunteer.objects.get(id=current_user)
    else:
        vol = Volunteer.objects.create(
            id=current_user
            )
        vol.save()
    return render(request, 'WeCareApp/profile.html', {'user_email':current_user.email})

@login_required
def signoutView(request):
    logout(request)
    return HttpResponseRedirect("/")


#
# @login_required
# def editTarget(request):
#     if request.method == 'POST':
#         current_user = request.user
#         vol = Volunteer.objects.get(id=current_user)
#         new_name = request.POST.get('edit_name')
#         new_dob = request.POST.get('edit_dob')
#         vol.name = new_name
#         vol.dob = new_dob
#         vol.save()
#         return HttpResponseRedirect("/profile")
#     else:
#         return HttpResponseRedirect("/profile")



def customLogin(request):
    if request.method == 'POST':
        entered_email = request.POST.get('login_email')
        entered_password = request.POST.get('login_password')
        if User.objects.filter(username=entered_email).exists():
            pass
        else:
            return HttpResponseRedirect("/")
        user = authenticate(username=entered_email, password=entered_password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('profile')
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


def customSignUp(request):
    if request.method == 'POST':
        entered_name = request.POST.get('signup_name')
        entered_email = request.POST.get('signup_email')
        entered_password = request.POST.get('signup_password')
        entered_dob = request.POST.get('signup_dob')
        if User.objects.filter(username=entered_email).exists():
            return render(request, "WeCareApp/index.html",{"clickLogin":True,"error_message_login":"You already have an account. Try logging in."})
        else:
            user = User.objects.create_user(
                username = entered_email,
                password = entered_password,
                email = entered_email
                )
            vol = Volunteer.objects.create(
                id=user,
                name=entered_name,
                dob=entered_dob
                )
            user.save()
            vol.save()
            login(request, user)
            return HttpResponseRedirect("/profile")
    else:
        return HttpResponseRedirect("/")
