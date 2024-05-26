from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

# Create your views here.

def employeeView(request):
    emp ={
        'id': 123,
        'name': 'John',
        'sal':100000
    }
    data = Employee.objects.all();
    response = {'employee':list(data.values('name','id'))}

    return JsonResponse(response)