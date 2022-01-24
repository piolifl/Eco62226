from Ecovalores import Ecovalores
import pyRofex

class Operar(Ecovalores):
    def __init__(self):
        Ecovalores.__init__(self)

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


