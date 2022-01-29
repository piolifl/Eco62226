from Broker import EV_62226
from datetime import datetime

import pyRofex

class Consultar(EV_62226):
    def __init__(self):
        EV_62226.__init__(self)

    def precioLA(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.LAST])
        try:
            return var['marketData']['LA']['price']
        except:
            return 1000

    def precioBI(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.BIDS])
        try:
            return var['marketData']['BI'][0]['price']
        except:
            return 1000

    def precioOF(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.OFFERS])
        try:
            return var['marketData']['OF'][0]['price']
        except:
            return 1000
    
    def logRulos(self, texto:str):
        f = open('rulos.log','a')
        f.write( datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' | ' + texto + '\n' )
        f.close()

    def logRatios(self, texto:str):
        f = open('ratios.log','a')
        f.write( datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' | ' + texto + '\n' )
        f.close()
        

