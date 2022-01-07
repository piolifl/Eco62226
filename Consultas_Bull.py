import pyRofex

pyRofex._set_environment_parameter(
    "url", "https://api.bull.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex._set_environment_parameter(
    "ws", "wss://api.bull.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex.initialize(
user="20263866623",password="Aned0609",account="145710", environment=pyRofex.Environment.LIVE)

def market_data_handler(message):
    print("Market Data Message Received: {0}".format(message))


def order_report_handler(message):
    global status
    #print("Order Report Message Received: {0}".format(message))
    symbol = message['orderReport']['instrumentId']['symbol']
    side = message['orderReport']['side']
    price = message['orderReport']['price']
    qty = message['orderReport']['orderQty']
    status = message['orderReport']['status']
    cumQty = message['orderReport']['cumQty']
    leavesQty = message['orderReport']['leavesQty']
    avgPx = message['orderReport']['avgPx']
    if status == 'NEW':
        print('Abierta',symbol, side, price, qty, status, cumQty, leavesQty, avgPx)
    else:
        print('Cerrada',symbol, side, price, qty, status, cumQty, leavesQty, avgPx)


def error_handler(message):
    print("Error Message Received: {0}".format(message))

def exception_handler(e):
    print("Exception Occurred: {0}".format(e.message))

# Initiate Websocket Connection
pyRofex.init_websocket_connection(market_data_handler=market_data_handler,order_report_handler=order_report_handler,error_handler=error_handler,exception_handler=exception_handler)

# Instruments list to subscribe
instruments = ["DONov19", "DODic19"]
# Uses the MarketDataEntry enum to define the entries we want to subscribe to
entries = [pyRofex.MarketDataEntry.BIDS,pyRofex.MarketDataEntry.OFFERS,pyRofex.MarketDataEntry.LAST]

# Subscribes to receive market data messages **
#pyRofex.market_data_subscription(tickers=instruments,entries=entries)

# Subscribes to receive order report messages (default account will be used) **
pyRofex.order_report_subscription()

'''
Order Report Message Received: {'type': 'or', 'timestamp': 1641497282624, 'orderReport': {'orderId': 'O08k2bkTsQio-01465793', 'clOrdId': 'onIa9hj3HjPIdCKH', 'proprietary': 'ISV_PBCP', 'execId': 'MERVE08k2WuROv7h', 'accountId': {'id': '62226'}, 'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - GFGC180.FE - 24hs'}, 'price': 20.11, 'orderQty': 1, 'ordType': 'LIMIT', 'side': 'BUY', 'timeInForce': 'DAY', 'transactTime': '20220106-16:27:27.981-0300', 'avgPx': 0, 'lastPx': 0, 'lastQty': 0, 'cumQty': 0, 'leavesQty': 1, 'status': 'NEW', 'text': ' ', 'numericOrderId': '01465793', 'originatingUsername': 'ISV_MATRIZ4'}}

Order Report Message Received: {'type': 'or', 'timestamp': 1641497333569, 'orderReport': {'orderId': 'O08k2bkTsQio-01465793', 'clOrdId': 'WmtAX0lVZ7RTX0F2', 'proprietary': 'ISV_PBCP', 'execId': 'MERVE08k2WuROw5b', 'accountId': {'id': '62226'}, 'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - GFGC180.FE - 24hs'}, 'price': 20.11, 'orderQty': 1, 'ordType': 'LIMIT', 'side': 'BUY', 'timeInForce': 'DAY', 'transactTime': '20220106-16:28:53.554-0300', 'avgPx': 0, 'lastPx': 0, 'lastQty': 0, 'cumQty': 0, 'leavesQty': 1, 'iceberg': 'true', 'displayQty': 0, 'status': 'CANCELLED', 'text': 'Cancelled by Owner', 'numericOrderId': '01465793', 'origClOrdId': 'onIa9hj3HjPIdCKH', 'originatingUsername': 'ISV_MATRIZ4'}}

Order Report Message Received: {'type': 'or', 'timestamp': 1641497333571, 'orderReport': {'orderId': 'O08k2bkTsQio-01465793', 'clOrdId': 'onIa9hj3HjPIdCKH', 'proprietary': 'ISV_PBCP', 'execId': 'MERVE08k2WuROw5b', 'accountId': {'id': '62226'}, 'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - GFGC180.FE - 24hs'}, 'price': 20.11, 'orderQty': 1, 'ordType': 'LIMIT', 'side': 'BUY', 'timeInForce': 'DAY', 'transactTime': '20220106-16:28:53.554-0300', 'avgPx': 0, 'lastPx': 0, 'lastQty': 0, 'cumQty': 0, 'leavesQty': 1, 'status': 'CANCELLED', 'text': 'CANCELED', 'originatingUsername': 'ISV_MATRIZ4'}}
'''
