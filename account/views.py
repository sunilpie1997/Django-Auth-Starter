from django.shortcuts import render,get_object_or_404
from django.http import request
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import SetPasswordForm
from django.views.generic.edit import CreateView
from django.conf import settings
from .models import User

def profileView(request):
    return render(request,"profile.html")

"""
By default,form used for this view is PasswordChangeForm but it requires old password to be filled.
So,we will overide this to SetPasswordForm.

https://docs.djangoproject.com/en/3.1/topics/auth/default/#django.contrib.auth.views.PasswordChangeView

"""
class ChangePasswordView(PasswordChangeView):
    form_class=SetPasswordForm

