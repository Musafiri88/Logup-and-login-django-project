from django.shortcuts import render, redirect
from login.forms import SignUpForm

# Create your views here.
def home_page(request):
    ''' Home page function view '''
    return render(request, 'login/home.html')


def  signup_view(request):
    ''' Sig up function view '''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    else:
        form = SignUpForm()

    context = {
        'form': form
    }
    return render(request, 'login/signup.html', context)
