from Consultar import Consultar
from Operar import Operar
import pyRofex

pr = Consultar()
op = Operar()

a = pr.precioLA('MERV - XMEV - AL30 - CI')
if a[0]!=10000:
    print(a)
else:
    print('no lo lee')



 


#op.comprar  ( 'MERV - XMEV - AL30 - CI' , 1 , a / 100 - 0.5 )

'''order = pyRofex.send_order(ticker='MERV - XMEV - AL30 - CI',
                           side=pyRofex.Side.BUY,
                           size=1,
                           price= a - 0.5,
                           order_type=pyRofex.OrderType.LIMIT)



b = pyRofex.get_order_status(order["orders"]["clOrdId"])
print(b)'''

'''{'status': 'OK', 'orders': [{'orderId': 'O0AGJdrG7alU-00519351', 'clOrdId': 'P43WSKJA40ygo8Bz', 'proprietary': 'ISV_PBCP', 'execId': 'MERVE0AGJZ1Da7J4', 'accountId': {'id': '62226'}, 'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - AL30 - CI'}, 'price': 5554.5, 'orderQty': 1, 'ordType': 'LIMIT', 'side': 'BUY', 'timeInForce': 'DAY', 'transactTime': '20220516-11:48:11.502-0300', 'avgPx': 5554.5, 'lastPx': 5554.5, 'lastQty': 1, 'cumQty': 1, 'leavesQty': 0, 'iceberg': 'true', 'displayQty': 0, 'status': 'FILLED', 'text': ' ', 'numericOrderId': '00519351', 'originatingUsername': 'ISV_MATRIZ4'}'''


'''{'type': 'or', 'timestamp': 1652712422251, 'orderReport': {'orderId': 'O0AGJdrG7alU-00519351', 'clOrdId': 'P43WSKJA40ygo8Bz', 'proprietary': 'ISV_PBCP', 'execId': 'MERVE0AGJZ1Da4do', 'accountId': {'id': '62226'}, 'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - AL30 - CI'}, 'price': 5554.5, 'orderQty': 1, 'ordType': 'LIMIT', 'side': 'BUY', 'timeInForce': 'DAY', 'transactTime': '20220516-11:47:02.226-0300', 'avgPx': 0, 'lastPx': 0, 'lastQty': 0, 'cumQty': 0, 'leavesQty': 1, 'status': 'NEW', 'text': ' ', 'numericOrderId': '00519351', 'originatingUsername': 'ISV_MATRIZ4'}}'''

'''{'type': 'or', 'timestamp': 1652712491519, 'orderReport': {'orderId': 'O0AGJdrG7alU-00519351', 'clOrdId': 'P43WSKJA40ygo8Bz', 'proprietary': 'ISV_PBCP', 'execId': 'MERVE0AGJZ1Da7J4', 'accountId': {'id': '62226'}, 'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - AL30 - CI'}, 'price': 5554.5, 'orderQty': 1, 'ordType': 'LIMIT', 'side': 'BUY', 'timeInForce': 'DAY', 'transactTime': '20220516-11:48:11.502-0300', 'avgPx': 5554.5, 'lastPx': 5554.5, 'lastQty': 1, 'cumQty': 1, 'leavesQty': 0, 'iceberg': 'true', 'displayQty': 0, 'status': 'FILLED', 'text': ' ', 'numericOrderId': '00519351', 'originatingUsername': 'ISV_MATRIZ4'}}'''