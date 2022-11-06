import requests
from datetime import datetime as dt
import smtplib

MY_LAT = 12.9634
MY_LNG = 77.5855
my_position = (MY_LAT, MY_LNG)

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])
position_of_iss = (latitude, longitude)



parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


def day():
    response1 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response1.raise_for_status()
    day_data = response1.json()
    sunrise = int(day_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(day_data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise += 5
    sunset += 5
    return sunrise, sunset


main_data = day()


present_data = dt.now()

if MY_LNG-5 <= longitude <= MY_LNG+5 and MY_LAT-5 <= latitude <= MY_LAT+5:
    hours = present_data.hour.conjugate()
    if hours <= main_data[0] or hours >= main_data[1]:
        email = "qazmko.1331@gmail.com"
        password = "svdfbkckbnntresq"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs="harshavardhan4125965@gmail.com",
                msg="look up buddie is above you"
            )
