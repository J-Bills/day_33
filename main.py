import requests
import datetime

MY_LAT = 0
MY_LNG = 0

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# data=response.json()

# longitude = data.get('iss_position')['longitude']
# latitude = data.get('iss_position')['latitude']

# iss_position = (longitude, latitude)

# print(iss_position)

paramaters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted':0    
}

response = requests.get('https://api.sunrise-sunset.org/json', params=paramaters)
response.raise_for_status()

data=response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

stuff = (sunrise,sunset)

time_now = datetime.datetime.now()
print(stuff)
print(time_now)
