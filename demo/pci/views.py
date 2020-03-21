from django.shortcuts import render
from .models import TestingClass

# Create your views here.

def index(request):
    test = TestingClass.objects.all()
    return render(request, 'index.html', {'test':test})
