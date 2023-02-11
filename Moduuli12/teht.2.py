import requests
from geopy.geocoders import Nominatim

APIKEY = ""
user_location = input(" Enter your location: ")

geolocator = Nominatim(user_agent = "api", timeout = 3)
location = geolocator.geocode(str(user_location))

request = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(location.latitude) + "&lon=" + str(
    location.longitude) + "&appid=" + APIKEY + "&units=metric"

answer = requests.get(request).json()
print(answer["weather"][0]["main"])
print("Temperature: "+str(answer["main"]["temp"]) + "°C")
