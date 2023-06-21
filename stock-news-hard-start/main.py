import requests
import warnings
warnings.filterwarnings(action='ignore')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = "b4704c5a9d3d4e27b7410e2ae80a4c15"
STOCK_API_KEY = "SBJRVN7T1OQ7NQEZ"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_parameters = {
    'q':COMPANY_NAME,
    'apiKey':NEWS_API_KEY

}

stock_parameters = {
    'function':'TIME_SERIES_DAILY_ADJUSTED',
    'symbol':STOCK,
    'apikey':STOCK_API_KEY
}


stock_connection = requests.get(url=STOCK_ENDPOINT, params=stock_parameters, verify=False)
data = stock_connection.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]


yesterday_data = data_list[0]
yesterday_closing = yesterday_data['4. close']
print(yesterday_closing)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing = day_before_yesterday_data['4. close']



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



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

