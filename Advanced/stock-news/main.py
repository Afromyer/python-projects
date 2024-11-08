from twilio.rest import Client
import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

account_sid = 'ACad20a0270d5a75e12ab5ca2a96e935ff'
auth_token = os.getenv("AUTH_TOKEN")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
STOCK_DATA = "https://www.alphavantage.co/query?"
STOCK_DATA_API = "O5KQOD347VE520FV"
NEWS_DATA_API = "1e456b497d5945068b4d1e50684c503c"


def check_stock_price_change():
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_DATA_API
    }

    response = requests.get(STOCK_DATA, params=stock_parameters)
    response.raise_for_status()
    stock_data = response.json()["Time Series (Daily)"]
    stock_data_dates = list(stock_data.keys())
    open_price = float(stock_data[stock_data_dates[0]]["4. close"])
    close_price = float(stock_data[stock_data_dates[1]]["4. close"])
    percentage_difference = ((open_price - close_price) / open_price) * 100
    # print(f"Open: {open_price}\nClose: {close_price}")
    # print(percentage_difference)
    return round(percentage_difference, 2)


def get_stock_news():
    news_params = {
        "apikey": NEWS_DATA_API,
        "qInTitle": COMPANY_NAME,
    }
    response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    data = response.json()
    return data["articles"]


def send_stock_update():
    stock_news = get_stock_news()
    if len(stock_news) > 0:
        percentage_difference = check_stock_price_change()
        if percentage_difference < 0:
            stock_change = f"{STOCK}: 🔻{percentage_difference}%"
        else:
            stock_change = f"{STOCK}: 🔺{percentage_difference}%"
        messages = f"{stock_change}\n\n\n"
        count = 0
        for news in stock_news:
            if count < 3:
                headline = news["title"]
                brief = news["description"]
                url = news["url"]
                count += 1
                messages += f"Headline: {headline}\nBrief: {brief}\nRead More:\n{url}\n\n\n"

            else:
                break
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="+19472227091",
            to='+27680495232',
            body=messages
        )
        print(message.status)
    else:
        print("No news found")


if abs(check_stock_price_change()) >= 0:
    send_stock_update()
else:
    print("Stock difference too low")
