import requests
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_number = os.environ['MY_PERSONAL_NUMBER']
api_key = os.environ['TWILIO_API_KEY']
params = {
    "lat": "62.139660",
    "lon": "65.414772",
    "cnt": 4,
    "appid": api_key,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()

will_rain = False
weather_data = response.json()
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today.Bring an ☔",
        from_='+18305496934',
        to=my_number
    )
    print(message.sid)
