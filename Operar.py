from Broker import EV_62226
import pyRofex

class Operar(EV_62226):
    def __init__(self):
        EV_62226.__init__(self)

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
        



