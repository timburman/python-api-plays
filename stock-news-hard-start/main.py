import requests
import warnings
warnings.filterwarnings(action='ignore')
import smtplib

EMAIL = "pythontutorials69@gmail.com"
PASSWORD = "mbxmapngtkhvjkhw"

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

# The Difference between the closing of yeasterday and day before yesterday
difference = abs(float(yesterday_closing) - float(day_before_yesterday_closing))

# Percentage of difference
diff_percentage = (difference/float(yesterday_closing)) * 100
print(diff_percentage)

# If diff greater than 5%
if diff_percentage > 5:
    news_connection = requests.get(url=NEWS_ENDPOINT, params=news_parameters, verify=False)
    data_news = news_connection.json()['articles']
    three_article = data_news[:3]
    descriptions = [x['description'] for x in three_article]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)

        connection.sendmail(
            from_addr=EMAIL,
            to_addrs='crplayer181102@gmail.com',
            msg=f'Subject:Tesla News\n\n{descriptions}'
        )

    


