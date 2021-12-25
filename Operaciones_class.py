import pyRofex
import config

pyRofex._set_environment_parameter(
    "url", "https://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex._set_environment_parameter(
    "ws", "wss://api.eco.xoms.com.ar/", pyRofex.Environment.LIVE)
pyRofex.initialize(config.user,
                   config.password,
                   config.account,
                   environment=pyRofex.Environment.LIVE)

class OPERACIONES:
    def __init__(self, ticker):
        self.ticker = ticker  
    def precio_LA(self):
        try:
            instrumento = self.ticker
            var = pyRofex.get_market_data(instrumento,entries=[pyRofex.MarketDataEntry.LAST])
            instrumento = var['marketData']['LA']['price']
        except:
            instrumento = 1000
        return instrumento
    def cantidad_LA(self):
        try:
            instrumento = self.ticker
            var = pyRofex.get_market_data(instrumento,entries=[pyRofex.MarketDataEntry.LAST])
            instrumento = var['marketData']['LA'][0]['size']
        except:
            instrumento = 0
        return instrumento
    def precio_OF(self):
        try:
            instrumento = self.ticker
            var = pyRofex.get_market_data(instrumento,entries=[pyRofex.MarketDataEntry.OFFERS])
            instrumento = var['marketData']['OF'][0]['price']
        except:
            instrumento = 1000
        return instrumento
    def cantidad_OF(self):
        try:
            instrumento = self.ticker
            var = pyRofex.get_market_data(instrumento,entries=[pyRofex.MarketDataEntry.OFFERS])
            instrumento = var['marketData']['OF'][0]['size']
        except:
            instrumento = 0
        return instrumento
    def precio_BI(self):
        try:
            instrumento = self.ticker
            var = pyRofex.get_market_data(instrumento,entries=[pyRofex.MarketDataEntry.BIDS])
            instrumento = var['marketData']['BI'][0]['price']
        except:
            instrumento = 1000
        return instrumento
    def cantidad_BI(self):
        try:
            instrumento = self.ticker
            var = pyRofex.get_market_data(instrumento,entries=[pyRofex.MarketDataEntry.BIDS])
            instrumento = var['marketData']['BI'][0]['size']
        except:
            instrumento = 0
        return instrumento
    def vender(self,cantidad,precio):
        pyRofex.send_order(
            ticker=self.ticker,
            side=pyRofex.Side.SELL, 
            size=cantidad, 
            price=precio,            
            order_type=pyRofex.OrderType.LIMIT)   
        return self
    def comprar(self,cantidad,precio):
        pyRofex.send_order(
            ticker=self.ticker,
            side=pyRofex.Side.BUY, 
            size=cantidad, 
            price=precio,            
            order_type=pyRofex.OrderType.LIMIT)   
        return self
    def __str__(self):
        return self.ticker

class C180(OPERACIONES):
    pass
class C185(OPERACIONES):
    pass
class C190(OPERACIONES):
    pass
class C195(OPERACIONES):
    pass
class C200(OPERACIONES):
    pass
class C210(OPERACIONES):
    pass
class C220(OPERACIONES):
    pass
class C230(OPERACIONES):
    pass
class C240(OPERACIONES):
    pass
class C250(OPERACIONES):
    pass
class C260(OPERACIONES):
    pass
class C270(OPERACIONES):
    pass
class C280(OPERACIONES):
    pass
class C290(OPERACIONES):
    pass
class C300(OPERACIONES):
    pass
class C310(OPERACIONES):
    pass
class C320(OPERACIONES):
    pass
class C330(OPERACIONES):
    pass
class C340(OPERACIONES):
    pass
class C350(OPERACIONES):
    pass
class C360(OPERACIONES):
    pass

class V180(OPERACIONES):
    pass
class V185(OPERACIONES):
    pass
class V190(OPERACIONES):
    pass
class V195(OPERACIONES):
    pass
class V200(OPERACIONES):
    pass
class V210(OPERACIONES):
    pass
class V220(OPERACIONES):
    pass
class V230(OPERACIONES):
    pass
class V240(OPERACIONES):
    pass
class V250(OPERACIONES):
    pass
class V260(OPERACIONES):
    pass
class V270(OPERACIONES):
    pass
class V280(OPERACIONES):
    pass
class V290(OPERACIONES):
    pass
class V300(OPERACIONES):
    pass
class V310(OPERACIONES):
    pass
class V320(OPERACIONES):
    pass
class V330(OPERACIONES):
    pass
class V340(OPERACIONES):
    pass
class V350(OPERACIONES):
    pass
class V360(OPERACIONES):
    pass


class GGAL(OPERACIONES):
    pass
class YPFD(OPERACIONES):
    pass

class AL30(OPERACIONES):
    pass
class AL35(OPERACIONES):
    pass
class GD30(OPERACIONES):
    pass
class GD35(OPERACIONES):
    pass

class KO(OPERACIONES):
    pass
class AAPL(OPERACIONES):
    pass


ticker = {
    'opciones':{
        'call':{
            'FE':{
                '180': C180('MERV - XMEV - GFGC180.FE - 24hs'),
                '185': C185('MERV - XMEV - GFGC185.FE - 24hs'),
                '190': C190('MERV - XMEV - GFGC190.FE - 24hs'),
                '195': C195('MERV - XMEV - GFGC195.FE - 24hs'),
                '200': C200('MERV - XMEV - GFGC200.FE - 24hs'),
                '210': C210('MERV - XMEV - GFGC210.FE - 24hs'),
                '220': C220('MERV - XMEV - GFGC220.FE - 24hs'),
                '230': C230('MERV - XMEV - GFGC230.FE - 24hs'),
                '240': C240('MERV - XMEV - GFGC240.FE - 24hs'),
                '250': C250('MERV - XMEV - GFGC250.FE - 24hs'),
                '260': C260('MERV - XMEV - GFGC260.FE - 24hs'),
                '270': C270('MERV - XMEV - GFGC270.FE - 24hs'),
                '280': C280('MERV - XMEV - GFGC280.FE - 24hs'),
                '290': C290('MERV - XMEV - GFGC290.FE - 24hs'),
                '300': C300('MERV - XMEV - GFGC300.FE - 24hs'),
                '310': C310('MERV - XMEV - GFGC310.FE - 24hs'),
                '320': C320('MERV - XMEV - GFGC320.FE - 24hs'),
                '330': C330('MERV - XMEV - GFGC330.FE - 24hs'),
                '340': C340('MERV - XMEV - GFGC340.FE - 24hs'),
                '350': C350('MERV - XMEV - GFGC350.FE - 24hs'),
                '360': C360('MERV - XMEV - GFGC360.FE - 24hs')},
            'AB':{
                '180': C180('MERV - XMEV - GFGC180.AB - 24hs'),
                '185': C185('MERV - XMEV - GFGC185.AB - 24hs'),
                '190': C190('MERV - XMEV - GFGC190.AB - 24hs'),
                '195': C195('MERV - XMEV - GFGC195.AB - 24hs'),
                '200': C200('MERV - XMEV - GFGC200.AB - 24hs'),
                '210': C210('MERV - XMEV - GFGC210.AB - 24hs'),
                '220': C220('MERV - XMEV - GFGC220.AB - 24hs'),
                '230': C230('MERV - XMEV - GFGC230.AB - 24hs'),
                '240': C240('MERV - XMEV - GFGC240.AB - 24hs'),
                '250': C250('MERV - XMEV - GFGC250.AB - 24hs'),
                '260': C260('MERV - XMEV - GFGC260.AB - 24hs'),
                '270': C270('MERV - XMEV - GFGC270.AB - 24hs'),
                '280': C280('MERV - XMEV - GFGC280.AB - 24hs'),
                '290': C290('MERV - XMEV - GFGC290.AB - 24hs'),
                '300': C300('MERV - XMEV - GFGC300.AB - 24hs'),
                '310': C310('MERV - XMEV - GFGC310.AB - 24hs'),
                '320': C320('MERV - XMEV - GFGC320.AB - 24hs'),
                '330': C330('MERV - XMEV - GFGC330.AB - 24hs'),
                '340': C340('MERV - XMEV - GFGC340.AB - 24hs'),
                '350': C350('MERV - XMEV - GFGC350.AB - 24hs'),
                '360': C360('MERV - XMEV - GFGC360.AB - 24hs')}
            },
        'put':{
            'FE':{
                '180': V180('MERV - XMEV - GFGV180.FE - 24hs'),
                '185': V185('MERV - XMEV - GFGV185.FE - 24hs'),
                '190': V190('MERV - XMEV - GFGV190.FE - 24hs'),
                '195': V195('MERV - XMEV - GFGV195.FE - 24hs'),
                '200': V200('MERV - XMEV - GFGV200.FE - 24hs'),
                '210': V210('MERV - XMEV - GFGV210.FE - 24hs'),
                '220': V220('MERV - XMEV - GFGV220.FE - 24hs'),
                '230': V230('MERV - XMEV - GFGV230.FE - 24hs'),
                '240': V240('MERV - XMEV - GFGV240.FE - 24hs'),
                '250': V250('MERV - XMEV - GFGV250.FE - 24hs'),
                '260': V260('MERV - XMEV - GFGV260.FE - 24hs'),
                '270': V270('MERV - XMEV - GFGV270.FE - 24hs'),
                '280': V280('MERV - XMEV - GFGV280.FE - 24hs'),
                '290': V290('MERV - XMEV - GFGV290.FE - 24hs'),
                '300': V300('MERV - XMEV - GFGV300.FE - 24hs'),
                '310': V310('MERV - XMEV - GFGV310.FE - 24hs'),
                '320': V320('MERV - XMEV - GFGV320.FE - 24hs'),
                '330': V330('MERV - XMEV - GFGV330.FE - 24hs'),
                '340': V340('MERV - XMEV - GFGV340.FE - 24hs'),
                '350': V350('MERV - XMEV - GFGV350.FE - 24hs'),
                '360': V360('MERV - XMEV - GFGV360.FE - 24hs')},
            'AB':{
                '180': V180('MERV - XMEV - GFGV180.AB - 24hs'),
                '185': V185('MERV - XMEV - GFGV185.AB - 24hs'),
                '190': V190('MERV - XMEV - GFGV190.AB - 24hs'),
                '195': V195('MERV - XMEV - GFGV195.AB - 24hs'),
                '200': V200('MERV - XMEV - GFGV200.AB - 24hs'),
                '210': V210('MERV - XMEV - GFGV210.AB - 24hs'),
                '220': V220('MERV - XMEV - GFGV220.AB - 24hs'),
                '230': V230('MERV - XMEV - GFGV230.AB - 24hs'),
                '240': V240('MERV - XMEV - GFGV240.AB - 24hs'),
                '250': V250('MERV - XMEV - GFGV250.AB - 24hs'),
                '260': V260('MERV - XMEV - GFGV260.AB - 24hs'),
                '270': V270('MERV - XMEV - GFGV270.AB - 24hs'),
                '280': V280('MERV - XMEV - GFGV280.AB - 24hs'),
                '290': V290('MERV - XMEV - GFGV290.AB - 24hs'),
                '300': V300('MERV - XMEV - GFGV300.AB - 24hs'),
                '310': V310('MERV - XMEV - GFGV310.AB - 24hs'),
                '320': V320('MERV - XMEV - GFGV320.AB - 24hs'),
                '330': V330('MERV - XMEV - GFGV330.AB - 24hs'),
                '340': V340('MERV - XMEV - GFGV340.AB - 24hs'),
                '350': V350('MERV - XMEV - GFGV350.AB - 24hs'),
                '360': V360('MERV - XMEV - GFGV360.AB - 24hs')}
            }},

    'bonos':{
        '48':{
            'peso':{
                'al30':AL30('MERV - XMEV - AL30 - 48hs'),'gd30':GD30('MERV - XMEV - GD30 - 48hs'),
                'al35':AL35('MERV - XMEV - AL35 - 48hs'),'gd35':GD35('MERV - XMEV - GD35 - 48hs')},
            'mep':{
                'al30':AL30('MERV - XMEV - AL30D - 48hs'),'gd30':GD30('MERV - XMEV - GD30D - 48hs'),
                'al35':AL35('MERV - XMEV - AL35D - 48hs'),'gd35':GD35('MERV - XMEV - GD35D - 48hs')},
            'ccl':{
                'al30':AL30('MERV - XMEV - AL30C - 48hs'),'gd30':GD30('MERV - XMEV - GD30C - 48hs'),
                'al35':AL35('MERV - XMEV - AL35C - 48hs'),'gd35':GD35('MERV - XMEV - GD35C - 48hs')}},
        '24':{
            'peso':{
                'al30':AL30('MERV - XMEV - AL30 - 24hs'),'gd30':GD30('MERV - XMEV - GD30 - 24hs'),
                'al35':AL35('MERV - XMEV - AL35 - 24hs'),'gd35':GD35('MERV - XMEV - GD35 - 24hs')},
            'mep':{
                'al30':AL30('MERV - XMEV - AL30D - 24hs'),'gd30':GD30('MERV - XMEV - GD30D - 24hs'),
                'al35':AL35('MERV - XMEV - AL35D - 24hs'),'gd35':GD35('MERV - XMEV - GD35D - 24hs')},
            'ccl':{
                'al30':AL30('MERV - XMEV - AL30C - 24hs'),'gd30':GD30('MERV - XMEV - GD30C - 24hs'),
                'al35':AL35('MERV - XMEV - AL35C - 24hs'),'gd35':GD35('MERV - XMEV - GD35C - 24hs')}},
        'CI':{
            'peso':{
                'al30':AL30('MERV - XMEV - AL30 - CI'),'gd30':GD30('MERV - XMEV - GD30 - CI'),
                'al35':AL35('MERV - XMEV - AL35 - CI'),'gd35':GD35('MERV - XMEV - GD35 - CI')},
            'mep':{
                'al30':AL30('MERV - XMEV - AL30D - CI'),'gd30':GD30('MERV - XMEV - GD30D - CI'),
                'al35':AL35('MERV - XMEV - AL35D - CI'),'gd35':GD35('MERV - XMEV - GD35D - CI')},
            'ccl':{
                'al30':AL30('MERV - XMEV - AL30C - CI'),'gd30':GD30('MERV - XMEV - GD30C - CI'),
                'al35':AL35('MERV - XMEV - AL35C - CI'),'gd35':GD35('MERV - XMEV - GD35C - CI')}}
            },

    'acciones':{
        '48':{
            'ggal': GGAL('MERV - XMEV - GGAL - 48hs'),
            'ypfd': YPFD('MERV - XMEV - YPFD - 24hs')},
        'CI':{
            'ggal': GGAL('MERV - XMEV - GGAL - CI'),
            'ypfd': YPFD('MERV - XMEV - YPFD - CI')}
            },

    'cedear':{
        'aapl_48':(
            AAPL('MERV - XMEV - AAPL - 48hs'),
            AAPL('MERV - XMEV - AAPL - CI')),
        'ko_48':(
            KO('MERV - XMEV - KO - 48hs'),
            KO('MERV - XMEV - KO - CI'))
            }
    }




