import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data=response.json()

longitude = data.get('iss_position')['longitude']
latitude = data.get('iss_position')['latitude']

iss_position = (longitude, latitude)

print(iss_position)