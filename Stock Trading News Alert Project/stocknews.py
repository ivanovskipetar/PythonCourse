import os, requests
from twilio.rest import Client

ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
MY_NUMBER = os.getenv('MY_PERSONAL_NUMBER')
TWILIO_API_KEY = os.getenv('TWILIO_API_KEY')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = os.environ['NEWS_API_KEY']
STOCK_API_KEY = os.environ['STOCK_API_KEY']

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

stock_data = response.json()['Time Series (Daily)']
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_data_list[0]
day_before_yesterday_data = stock_data_list[1]

closing_price_yesterday = yesterday_data["4. close"]
closing_price_day_before_yesterday = day_before_yesterday_data["4. close"]

difference = float(closing_price_yesterday) - float(closing_price_day_before_yesterday)
emoji = None
if difference > 0:
    emoji = "🔼"
else:
    emoji = "🔽"
difference_percentage = round((difference / float(closing_price_yesterday)) * 100)

if abs(difference_percentage) > 5:
    news_params = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    data = news_response.json()
    articles_list = data["articles"]
    first_three_articles = articles_list[:3]

    formatted_articles = [f"{STOCK}: {emoji}{difference_percentage}%\nHeadline: {article['title']} \nBrief: {article['description']}" for article in first_three_articles]

    for article in formatted_articles:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
            body=article,
            from_='+18305496934',
            to=MY_NUMBER
        )
        print(message.sid)