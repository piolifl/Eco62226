import time
from datetime import datetime
import pyRofex

pyRofex._set_environment_parameter("url", "https://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex._set_environment_parameter("ws", "wss://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex.initialize(user="20263866623", password="APP883dR#", account="62226", environment=pyRofex.Environment.LIVE)

md = pyRofex.get_market_data(ticker="MERV - XMEV - AL30 - CI",
                             entries=[pyRofex.MarketDataEntry.BIDS])

order = pyRofex.send_order(ticker="MERV - XMEV - AL30 - CI",
                           side=pyRofex.Side.BUY,
                           size=10,
                           price=md["marketData"]["BI"][0]["price"],
                           order_type=pyRofex.OrderType.LIMIT)

order_status = pyRofex.get_order_status(order["order"]["clientId"])