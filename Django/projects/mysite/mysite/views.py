from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'../templates/index.html')

def about(request):
    print(request.GET.get('text','default'))
    return HttpResponse("This is about Section")

def links(request):
    return HttpResponse("hello")