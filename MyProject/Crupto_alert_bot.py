import requests
import pandas
# from scipy import *
# import time

coin_api_key = '6B7918F9-D6F3-4353-B3B7-2343E54D6F67'

def Coinprices(crypto):
    url = 'https://rest.coinapi.io/v1/exchangerate/{0}/USD'.format(crypto)
    headers = {'X-CoinAPI-Key': coin_api_key}
    # response = requests.get(url, headers = headers)
    # content = response.json()
    current_price = content['rate']
    current_time = content['time']

    url = 'https://rest.coinapi.io/v1/ohlcv/{0}/USD/latest?period_id=1DAY&limit=30'.format(crypto)
    headers = {'X-CoinAPI-Key': coin_api_key}
    # response = requests.get(url, headers = headers)
    # content = response.json()
    df_30 = pd.DataFrame(content)

    url = 'https://rest.coinapi.io/v1/ohlcv/{0}/USD/latest?period_id=1DAY&limit=90'.format(crypto)
    headers = {'X-CoinAPI-Key' : coin_api_key}
    response = requests.get(url, headers=headers)
    content = response.json()
    df_90 = pd.DataFrame(content)

    day_30_percentile = stats.percentileofscore(df_30.price_close, current_price)
    day_90_percentile = stats.percentileofscore(df_90.price_close, current_price)
    
    return {'current_price': current_price, 'day_30_percentile': day_30_percentile, 'day_90_percentile': day_90_percentile}

def createMessage(cyrpto, current_price, day_30_percentile):
        if day_30_percentile <= 20:
            status = 'BARGAIN'
        elif day_30_percentile <= 80:
            status = 'TYPICAL BUY'
        else:
            status = 'RIP-OFF'

    percentile_formatted = "{:.1%}".format(day_30_percentile/100)
    current_price_formatted = '${:,.2f}'.format(current_price)

    message = '{0} is a {1} today. The current price of {2} is higher than {3} of closing prices during the last 30 days.'.format(crypto, status, current_price_formatted, percentile_formatted)
    return(message)

