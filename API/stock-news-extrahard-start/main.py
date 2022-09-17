import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_api = "cf55f43790a14c95a14e6b8e12256c6b"





## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "interval": "5min",
    "apikey": "8BCSFUXXXW4H507A",
}
stock = requests.get(url=STOCK_ENDPOINT, params=parameter)
data = stock.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_close_price = data_list[0]["4. close"]
print(yesterday_close_price)


#  Get the day before yesterday's closing stock price
day_before_yesterday_closing_price = data_list[1]["4. close"]
print(day_before_yesterday_closing_price)
# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_close_price) - float(day_before_yesterday_closing_price))
print(difference)
#  Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percentage = (difference/float(yesterday_close_price))*100
print(difference_percentage)
#  If TODO4 percentage is greater than 5 then print("Get News").
# if difference_percentage > 4:



## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#  Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME

new_parameter = {
    "apiKey": "cf55f43790a14c95a14e6b8e12256c6b",
    "qInTitle": COMPANY_NAME,
}
news = requests.get(NEWS_ENDPOINT, params=new_parameter)
# Use Python slice operator to create a list that contains the first 3 articles. Hint: ttps://stackoverflow.com/questions/509211/understanding-slice-notation

data = news.json()["articles"][:3]


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# Create a new list of the first 3 article's headline and description using list comprehension.
formatted_news = [f"headline: {article['title']}. \nBrief: {article['description']}" for article in data]
print(formatted_news)
# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
