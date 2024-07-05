from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import requests
from .models import Flight
from rest_framework.decorators import api_view
# Create your views here.



def login(request):
    print("Welcome "+ request.method)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        if len(username)>0 and len(password)>0:
            response = requests.post('http://127.0.0.1:8000/api-token-auth/',data={'username':username, 'password':password})
            print("Token API response status: ", response.status_code)


            if response.status_code == 200:
                token = response.json().get('token')
                request.session['token'] = token
                messages.success(request,'Login successful')
                return redirect('/home')
            else:
               messages.error(request,'Invalid username or password')
        else:  
          messages.error(request,'please enter valid data')      
    return render(request,"login.html")


def home(request):
    return render(request, "home.html")


def all_flights(request):
    token = request.session.get('token')
    if not token: 
        messages.error(request,'You are not authenticated')
        return redirect('/login')
    
    headers = {'Authorization': f'Token {token}'}
    response = requests.get('http://127.0.0.1:8000/flightServices/flights/', headers=headers)
    print("Flights API response status: ", response.status_code)
    print("Flights API response: ", response.json())


    if response.status_code == 200:
        flights = response.json()
        
    else:
        flights = []    

    return render(request, 'all_flights.html' ,{'flights':flights})


def find_flights(request):
    print("Entered findFlights")
    token = request.session.get('token')
    if not token: 
        messages.error(request,'You are not authenticated')
        return redirect('/login')
    
    if request.method == 'POST':
        departure_city = request.POST.get('departureCity')
        arrival_city = request.POST.get('arrivalCity')
        date_of_departure= request.POST.get('dateOfDeparture')

        headers = {'Authorization': f'Token {token}'}
        url = 'http://127.0.0.1:8000/flightServices/findFlights/'
        data = {
            'departureCity': departure_city,
            'arrivalCity': arrival_city,
            'dateOfDeparture': date_of_departure,
        }
        
        print("API request:" + str(url) + " token "+ str(headers) + " data : "+ str(data))

        response = requests.post(url, json=data ,headers=headers)

        print("API response:" + str(response.json))
        if response.status_code == 200:
            flights = response.json()
            print("Flights data:" + str(flights))
            return render(request,'find_flights_result.html', {'flights':flights})
        else:
            print(" error response.status_code:" + str(response.status_code))
            error_message = f"Failed to fetch flights: {response.status_code}"
            return redirect('/Result', {'error_message': error_message})
    else:
        print(" ENTERED NOT POST METHOD")

    return render(request, "find_flights.html" )


def find_flights_result(request):
    flights = Flight.objects.all()
    print(flights)
    return render(request, 'find_flights_result.html',{'flights':flights})


def reserve_flight(request):
    return render(request, 'reserve_flights.html')

def confirm_flight(request):
    return render(request, 'confirm_flight.html')