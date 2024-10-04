from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def calculator(request):
    return render(request, 'Calculator.html')