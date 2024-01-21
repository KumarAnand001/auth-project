from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from testApp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):

    return render(request, 'testApp/home.html')

@login_required
def java_exam_view(request):

    return render(request, 'testApp/javaexam.html')

def python_exam_view(request):

    return render(request, 'testApp/pythonexam.html')

def apptitude_exam_view(request):

    return render(request, 'testApp/apptitudeexam.html')

def logout_view(request):

    return render(request, 'testApp/logout.html')

def signup_view(request):

    form = SignUpForm()
    if request.method == 'POST':
        
        form = SignUpForm(request.POST)
        # if form.is_valid():
        #     form.save() 
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    
    return render(request, 'testApp/signup.html', {'form':form})
