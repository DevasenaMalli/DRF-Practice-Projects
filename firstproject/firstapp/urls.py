from . import views
from django.urls import path

urlpatterns = [
    path('emps/',views.employeeView),
]

