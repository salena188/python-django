from django.shortcuts import render


def index(request):
    print("this is my index method")
    return render(request,'index.html')

def student_index(request):
    return render(request,'student_index.html')

def landing(request):
    return render(request,'landing.html')