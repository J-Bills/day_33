import requests
from datetime import datetime
import time
import config

starttime = time.monotonic()
while True:
    MY_LAT = int(51.507351) # Your latitude
    MY_LONG = int(-0.127758) # Your longitude

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # iss_latitude = float(data["iss_position"]["latitude"])
    # iss_longitude = float(data["iss_position"]["longitude"])
    
    iss_latitude = int(50.10023)
    iss_longitude = int(2.14553)

    #Your position is within +5 or -5 degrees of the ISS position.
    if iss_latitude in range(MY_LAT - 5, MY_LAT + 5) and iss_longitude in range(MY_LONG - 5, MY_LONG + 5):
        print('here')
        
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now()
        
        print(sunrise, ': sunrise')
        print(sunset, ': sunset')
        print(time_now.hour,': now')

        if (time_now.hour < sunset) and (time_now.hour > sunrise):
            print('sending')
            email = config.email_setup()
            config.email_sending(email,"The ISS is above!")

        #If the ISS is close to my current position
        # and it is currently dark
        # Then send me an email to tell me to look up.
        # BONUS: run the code every 60 seconds.
    time.sleep(60.0 - ((time.monotonic() - starttime) % 60.0))





