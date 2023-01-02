import requests
from datetime import datetime, timedelta
from twilio.rest import Client

account_sid = "AC630e6a2c542d9c7730c0bdf40cdf3f09"
auth_token = "4f466656bc9eae465e4edb923be397cb"
api_key = "cbafdfd562a02dffdff2addbd7c2952e"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = "QDDMILDTOGY6NQ1T"
NEWS_KEY = "8070b5481d524df7ac8f396153f821bf"
yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
before_yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
smile = ""
headlines = []
briefs = []

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_KEY
}

parameters_news = {
    "apiKey": NEWS_KEY,
    "q": COMPANY_NAME,
    "from": yesterday,
    "to": yesterday,
    "sortBy": "popularity",
    "language": "en"
}


def send_message():
    for i in range(0, 3):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"{STOCK} {smile} \n"
                     f"{headlines[i]}",
                from_="+19794288972",
                to="+971585920990"
            )
        print(message.status)


def get_news():
    global headlines
    global briefs
    news = requests.get(NEWS_ENDPOINT, params=parameters_news)
    data_news = news.json()
    articles = data_news['articles']
    for i in range(0, 3):
        headlines.append(articles[i]["title"])
    send_message()


def get_price():
    stocks_price = requests.get(STOCK_ENDPOINT, params=parameters)
    data = stocks_price.json()
    price_yesterday = float(data['Time Series (Daily)'][yesterday]['4. close'])
    price_before_yesterday = float(data['Time Series (Daily)'][before_yesterday]['4. close'])
    positive_difference = abs(price_yesterday - price_before_yesterday)
    global smile
    if price_yesterday > price_before_yesterday:
        smile = "🔺"
    else:
        smile = "🔻"
    # five_percent = round(abs(((price_yesterday-price_before_yesterday)/price_before_yesterday) * 100), 2)
    five_percent = 5.0
    if five_percent >= 5:
        get_news()


get_price()

