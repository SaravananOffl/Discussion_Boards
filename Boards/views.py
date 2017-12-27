from django.shortcuts import render
from django.http import HttpResponse
from Boards.models import *
# Create your views here.
def index(request):
    return render(request,'Boards/home.html')

