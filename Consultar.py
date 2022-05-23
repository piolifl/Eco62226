from Broker import ECO_62226
from Broker import BCCH_2474
from datetime import datetime
import pyRofex

class Consultar(ECO_62226):
    def __init__(self):
        ECO_62226.__init__(self)

    def precioLA(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.LAST])
        try: pr = var['marketData']['LA']['price'] 
        except: pr = 10000
        la = 1000
        return pr, la

    def precioBI(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.BIDS])
        try: pr = var['marketData']['BI'][0]['price']
        except: pr = 10000
        try: bi = var['marketData']['BI'][0]['size']
        except: bi = 0
        return pr, bi
        '''try: return var['marketData']['BI'][0]['price']
        except: return 10000'''

    def precioOF(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.OFFERS])
        try: pr = var['marketData']['OF'][0]['price']
        except: pr = 10000
        try: of = var['marketData']['OF'][0]['size']
        except: of = 0
        return pr, of





    '''def bidsBI(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.BIDS])
        try: return var['marketData']['BI'][0]['size']
        except: return 0

    def offersOF(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.OFFERS])
        try: return var['marketData']['OF'][0]['size']
        except: return 0

    def logRulos(self, texto:str):
        f = open('rulos.log','a')
        f.write( datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' | ' + texto + '\n' )
        f.close()

    def logRatios(self, texto:str):
        f = open('ratios.log','a')
        f.write( datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' | ' + texto + '\n' )
        f.close()
        
class Consultar2(BCCH_2474):
    def __init__(self):
        BCCH_2474.__init__(self)

    def precioLA(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.LAST])
        try: return var['marketData']['LA']['price']
        except: return 1000

    def precioBI(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.BIDS])
        try: return var['marketData']['BI'][0]['price']
        except: return 1000

    def precioOF(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.OFFERS])
        try: return var['marketData']['OF'][0]['price']
        except: return 1000
    
    def bidsBI(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.BIDS])
        try: return var['marketData']['BI'][0]['size']
        except: return 0.0

    def offersOF(self,ticker=str):
        var = pyRofex.get_market_data(ticker,entries=[pyRofex.MarketDataEntry.OFFERS])
        try: return var['marketData']['OF'][0]['size']
        except: return 0.0
    
    def logRulos(self, texto:str):
        f = open('rulos.log','a')
        f.write( datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' | ' + texto + '\n' )
        f.close()

    def logRatios(self, texto:str):
        f = open('ratios.log','a')
        f.write( datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' | ' + texto + '\n' )
        f.close()'''

