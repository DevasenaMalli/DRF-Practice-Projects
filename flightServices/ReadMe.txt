DRF Api 1: Fetch API Key
=========================
Request Type: POST
http://127.0.0.1:8000/api-token-auth/
{
    "username":"test",
    "password":"devipass"

}
Response :
{
    "token": "5bb076730aa7ca59712a8766b000f6391511ee4a"
}

DRF Api 2: Fetch Flight ID
==========================
Request Type: POST
Add Header:
Authorization : Token 5bb076730aa7ca59712a8766b000f6391511ee4a
https://127.0.0.1:8000/flightServices/flights/
{
    "flightNumber": "AAA",
    "operatingAirline":"American",
    "arrivalCity": "Newyork",
    "dateOfDeparture": "2023-11-11",
    "estimatedTimeOfDeparture": "11:11:00"
}

{
    "id": 22,
    "flightNumber": "AAA",
    "operatingAirline": "American",
    "departureCity": null,
    "arrivalCity": "Newyork",
    "dateOfDeparture": "2023-11-11",
    "estimatedTimeOfDeparture": "11:11:00"
}

DRF Api 3: Fetch Flight ID
===========================
Request Type: POST