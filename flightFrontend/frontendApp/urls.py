from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login, name='login'),
    path('home/',views.home, name='home'),
    path('Allflights/',views.all_flights, name='all_flights'),
    path('Findflights/',views.find_flights, name='find_flights'),
    path('Result/', views.find_flights_result, name='find_flights_result'),

    path('Reserveflight/',views.reserve_flight, name='reserve_flight'),
    path('Confirmflight/',views.confirm_flight, name='confirm_flight')
    
]