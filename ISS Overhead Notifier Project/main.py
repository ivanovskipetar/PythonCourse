import requests, smtplib, time
from datetime import datetime

MY_LAT = 42.202030  # Your latitude
MY_LONG = 22.333950  # Your longitude
MY_EMAIL = ""
PASSWORD = ""


def is_within_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


def is_night():
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

    time_now = datetime.now().hour

    return time_now >= sunset and time_now <= sunrise


while True:
    time.sleep(60)
    # If the ISS is close to my current position
    if is_within_range():
        # and it is currently dark
        if is_night():
            # Then send me an email to tell me to look up.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=MY_EMAIL,
                                    msg="Subject:ISS Notifier!\n\nLook UP! The International Space Station is above you!")
    # BONUS: run the code every 60 seconds.
