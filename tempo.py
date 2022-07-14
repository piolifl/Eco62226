
import time
from datetime import datetime
import pyRofex

pyRofex._set_environment_parameter("url", "https://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex._set_environment_parameter("ws", "wss://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex.initialize(user="20263866623", password="APP883dR#", account="62226", environment=pyRofex.Environment.LIVE)


def market_data_handler(message):
    global precios
    #print("Market Data Message Received: {0}".format(message))
    sym = message['instrumentId']['symbol']
    last = 1000 if not message['marketData']['LA'] else message['marketData']['LA']['price']
    bid = None if not message['marketData']['BI'] else message['marketData']['BI'][0]['price']
    bidSize = 0 if not message['marketData']['BI'] else message['marketData']['BI'][0]['size']
    ask = None if not message['marketData']['OF'] else message['marketData']['OF'][0]['price']
    askSize = 0 if not message['marketData']['OF'] else message['marketData']['OF'][0]['size']
    
    precios = [ sym,last,bid,ask]
    return precios
    #print(precios)
    #if last > 1000: print(last)
    #return last

'''def order_report_handler(message):
    print("Order Report Message Received: {0}".format(message))
def error_handler(message):
    print("Error Message Received: {0}".format(message))
def exception_handler(e):
    print("Exception Occurred: {0}".format(e.message))'''

# Initiate Websocket Connection
pyRofex.init_websocket_connection(market_data_handler=market_data_handler,
                                  #order_report_handler=order_report_handler,
                                  #error_handler=error_handler,
                                  #exception_handler=exception_handler
                                  )

# Instruments list to subscribe
instruments = ["MERV - XMEV - AL30C - 48hs", "MERV - XMEV - GD30C - 48hs", ]

# Uses the MarketDataEntry enum to define the entries we want to subscribe to
entries = [
    pyRofex.MarketDataEntry.BIDS,
    pyRofex.MarketDataEntry.OFFERS,
    pyRofex.MarketDataEntry.LAST,
    pyRofex.MarketDataEntry.CLOSING_PRICE,
    pyRofex.MarketDataEntry.OPENING_PRICE,
    pyRofex.MarketDataEntry.HIGH_PRICE,
    pyRofex.MarketDataEntry.LOW_PRICE,
    pyRofex.MarketDataEntry.SETTLEMENT_PRICE,
    pyRofex.MarketDataEntry.NOMINAL_VOLUME,
    pyRofex.MarketDataEntry.TRADE_EFFECTIVE_VOLUME,
    pyRofex.MarketDataEntry.TRADE_VOLUME,
    pyRofex.MarketDataEntry.OPEN_INTEREST
           ]

# Subscribes to receive market data messages **
pyRofex.market_data_subscription(tickers=instruments, entries=entries)

# Subscribes to receive order report messages (default account will be used) **
#pyRofex.order_report_subscription()




'''Market Data Message Received: {'type': 'Md', 'timestamp': 1657742624392, 'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - GD30C - 48hs'}, 'marketData': {'BI': [{'price': 19.25, 'size': 250000}], 'OF': [{'price': 19.99, 'size': 110729}], 'OP': 19.5, 'NV': 12765566, 'HI': 20.14, 'TV': None, 'LO': 19.5, 'SE': {'price': 19.99}, 'EV': 2553145.99, 'LA': {'price': 19.99, 'size': 169271, 'date': 1657742410000}, 'OI': None, 'CL': {'price': 19.7}}}
MERV - XMEV - GD30C - 48hs 19.99 250000 19.25 19.99 110729'''