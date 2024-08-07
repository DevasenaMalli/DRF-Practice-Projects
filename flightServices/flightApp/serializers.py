from rest_framework import serializers
from flightApp.models import Flight,Passenger,Reservation
import re


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


    def validate_flightNumber(self,flightNumber):
        if(re.match("^[a-zA-Z0-9]*$",flightNumber)==None):
             raise serializers.ValidationError("Invalid Flight Number.Make sure it is alpha numeric")
        return flightNumber


    def validate(self,data):
         print("validate")
         print(data['flightNumber'])
         print(data)
         return data 

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

 
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'       

class FlightRequestSerializer(serializers.Serializer):
    departureCity = serializers.CharField(max_length=50)
    arrivalCity = serializers.CharField(max_length=50)
    dateOfDeparture = serializers.DateField()