from Broker import ECO_62226
from Broker import BCCH_2474
import pyRofex

class Operar(ECO_62226):
    def __init__(self):
        ECO_62226.__init__(self)

    def comprar(self,ticker=str,cantidad=float,precio=float):
        pyRofex.send_order(
            ticker=ticker,
            side=pyRofex.Side.BUY, 
            size=cantidad, 
            price=precio,            
            order_type=pyRofex.OrderType.LIMIT)
        return
    
    def vender(self,ticker=str,cantidad=float,precio=float):
        pyRofex.send_order(
            ticker=ticker,
            side=pyRofex.Side.SELL, 
            size=cantidad, 
            price=precio,            
            order_type=pyRofex.OrderType.LIMIT)
        return
        
class Operar2(BCCH_2474):
    def __init__(self):
        BCCH_2474.__init__(self)

    def comprar(self,ticker=str,cantidad=float,precio=float):
        pyRofex.send_order(
            ticker=ticker,
            side=pyRofex.Side.BUY, 
            size=cantidad, 
            price=precio,            
            order_type=pyRofex.OrderType.LIMIT)
        return
    
    def vender(self,ticker=str,cantidad=float,precio=float):
        pyRofex.send_order(
            ticker=ticker,
            side=pyRofex.Side.SELL, 
            size=cantidad, 
            price=precio,            
            order_type=pyRofex.OrderType.LIMIT)
        return


