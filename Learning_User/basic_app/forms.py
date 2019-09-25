from django import forms

from django.contrib.auth.models import User

from .models import UserProfile


class userform(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():

        model = User
        fields= ('username','password','email')


class Userprofileform(forms.ModelForm):

    class Meta():

        model = UserProfile
        fields =  ('portfolio_site','profile_pic')
