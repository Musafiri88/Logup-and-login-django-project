from django.shortcuts import render, redirect
from login.forms import SignUpForm

# Create your views here.
def home_page(request):
    ''' Home page function view '''
    return render(request, 'login/home.html')
