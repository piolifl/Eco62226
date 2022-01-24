from Ecovalores import Ecovalores
import pyRofex

class Consultar(Ecovalores):
    def __init__(self):
        Ecovalores.__init__(self)

    def precioLA(self,ticker=str) -> dict:
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.LAST])
        try:
            return var['marketData']['LA']['price']
        except:
            return 1000

    def precioBI(self,ticker=str) -> dict:
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.BIDS])
        try:
            return var['marketData']['BI'][0]['price']
        except:
            return 1000

    def precioOF(self,ticker=str) -> dict:
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.OFFERS])
        try:
            return var['marketData']['OF'][0]['price']
        except:
            return 1000

