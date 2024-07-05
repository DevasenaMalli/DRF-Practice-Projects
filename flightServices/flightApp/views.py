from django.shortcuts import render
from flightApp.models import Flight,Passenger,Reservation
from flightApp.serializers import FlightRequestSerializer, FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def find_flights(request):
    departure_city=request.data.get('departureCity')
    arrival_city=request.data.get('arrivalCity')
    date_of_departure=request.data.get('dateOfDeparture')
    
    print("request:" + str(departure_city))
    print("request:" + str(arrival_city))
    print("request:" + str(date_of_departure))


    if departure_city and arrival_city and date_of_departure:
        flights = Flight.objects.filter(
          departureCity = departure_city,
          arrivalCity = arrival_city,
          dateOfDeparture = date_of_departure

          
        )
    else:
        flights = Flight.objects.none()

    serializer = FlightSerializer(flights,many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def find_flight_by_id(request, id):
    flight = get_object_or_404(Flight, id=id)
    serializer = FlightSerializer(flight)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight = Flights.objects.get(id=request.data['flightId'])
    
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName'] 
    passenger.middleName = request.data['middleName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = paasenger

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)



# Create your views here.
class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['departureCity', 'arrivalCity','dateOfDeparture']
    permission_classes = [IsAuthenticated]


class PassengerViewSet(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer
    permission_classes = [IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    permission_classes = [IsAuthenticated]