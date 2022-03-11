from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, ProfileForm

# Create your views here.

def Home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Dashboard(request):
    template = loader.get_template('dashboard.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Signup(request):
    if request.method == 'POST':
        # process the form data
        form = UserForm(request.POST)
        if form.is_valid():
            # validate the data
            user = form.save()
            login(request, user)
            # redirect to the new URL
            # return redirect('profile')
            return HttpResponseRedirect('/profile')
    else:
#       # option 1
        # create a blank form
        form = UserForm(initial={'email': '@gmail.com'})
    return render(request, 'signup.html', {'form': form})
#       # option 2
#    ''''
#       template = loader.get_template('signup.html')
#       context = {
#           'form': form
#       }
#    return HttpResponse(template.render(context, request))
#    '''

def Profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboad')
    else:
        form = ProfileForm()
    return render(request, 'signup.html', {'form': form})
