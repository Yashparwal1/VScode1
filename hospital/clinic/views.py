from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
def hello(request):
    return render(request,'hello.html', {'name':'yash'})

# def index(request):
#     return HttpResponse("This is home page")

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')