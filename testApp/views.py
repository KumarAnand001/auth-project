from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
