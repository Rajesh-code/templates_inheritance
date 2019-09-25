from django.shortcuts import render
from .forms import Userprofileform, userform


def index(request):

    return render(request, 'basic_app/index.html')


def register(request):

    registered = False

    if request.method =='POST':

        user_form = userform(data = request.POST)
        profile_form  = Userprofileform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user  # one to one relationship with the User form, so that database will not assume for multiple inheritance

            if 'profile_pic' in request.FILES:

                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:

            print(user_form.errors, profile_form.errors)
    else:
        user_form = userform()
        profile_form = Userprofileform()
    return render(request, 'basic_app/registration.html',
                  {'user_form':user_form, 'profile_form':profile_form, 'registered': registered})



# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def user_login(request):

    if request.method =='post':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)

        if user:

            if user.is_active:

                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:

                return HttpResponse('user is inactive')
        else:

            print('wrong passwords')

            return HttpResponse('Invalid Credentials')
    else:

        return render(request, 'basic_app/login.html',{})


@login_required
def user_logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse('You are logged in Nice!')
