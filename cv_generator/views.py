from django.shortcuts import render
from .forms import Userform,EditProfileForm
from .models import User
from django.views.generic.edit import CreateView,UpdateView

class Signup(CreateView):
    form_class = Userform
    model = User
    success_url = '/signin/'
    template_name = 'enroll/signup.html'

class Editprofile(UpdateView):
    model = User
    form_class=EditProfileForm
    template_name = 'enroll/editprofile.html'
    success_url='/homepage/'

def homepage(request):
    return render(request,"enroll/homepage.html")

