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

class CALL(OPERACIONES):
    pass
class PUT(OPERACIONES):
    pass

class GGAL(OPERACIONES):
    pass
class YPFD(OPERACIONES):
    pass

class AL30(OPERACIONES):
    pass
class AE38(OPERACIONES):
    pass
class AL29(OPERACIONES):
    pass
class AL35(OPERACIONES):
    pass
class AL41(OPERACIONES):
    pass

class GD30(OPERACIONES):
    pass
class GD29(OPERACIONES):
    pass
class GD35(OPERACIONES):
    pass
class GD38(OPERACIONES):
    pass
class GD41(OPERACIONES):
    pass

class S31E2(OPERACIONES):
    pass
class S28F2(OPERACIONES):
    pass
class S31M2(OPERACIONES):
    pass
class S29A2(OPERACIONES):
    pass

class KO(OPERACIONES):
    pass
class AAPL(OPERACIONES):
    pass

ticker = {
    'opciones':{
        'call':{
            'FE':{
                '180': CALL('MERV - XMEV - GFGC180.FE - 24hs'),
                '185': CALL('MERV - XMEV - GFGC185.FE - 24hs'),
                '190': CALL('MERV - XMEV - GFGC190.FE - 24hs'),
                '195': CALL('MERV - XMEV - GFGC195.FE - 24hs'),
                '200': CALL('MERV - XMEV - GFGC200.FE - 24hs'),
                '210': CALL('MERV - XMEV - GFGC210.FE - 24hs'),
                '220': CALL('MERV - XMEV - GFGC220.FE - 24hs'),
                '230': CALL('MERV - XMEV - GFGC230.FE - 24hs'),
                '240': CALL('MERV - XMEV - GFGC240.FE - 24hs'),
                '250': CALL('MERV - XMEV - GFGC250.FE - 24hs'),
                '260': CALL('MERV - XMEV - GFGC260.FE - 24hs'),
                '270': CALL('MERV - XMEV - GFGC270.FE - 24hs'),
                '280': CALL('MERV - XMEV - GFGC280.FE - 24hs'),
                '290': CALL('MERV - XMEV - GFGC290.FE - 24hs'),
                '300': CALL('MERV - XMEV - GFGC300.FE - 24hs'),
                '310': CALL('MERV - XMEV - GFGC310.FE - 24hs'),
                '320': CALL('MERV - XMEV - GFGC320.FE - 24hs'),
                '330': CALL('MERV - XMEV - GFGC330.FE - 24hs'),
                '340': CALL('MERV - XMEV - GFGC340.FE - 24hs'),
                '350': CALL('MERV - XMEV - GFGC350.FE - 24hs'),
                '360': CALL('MERV - XMEV - GFGC360.FE - 24hs')},
            'AB':{
                '180': CALL('MERV - XMEV - GFGC180.AB - 24hs'),
                '185': CALL('MERV - XMEV - GFGC185.AB - 24hs'),
                '190': CALL('MERV - XMEV - GFGC190.AB - 24hs'),
                '195': CALL('MERV - XMEV - GFGC195.AB - 24hs'),
                '200': CALL('MERV - XMEV - GFGC200.AB - 24hs'),
                '210': CALL('MERV - XMEV - GFGC210.AB - 24hs'),
                '220': CALL('MERV - XMEV - GFGC220.AB - 24hs'),
                '230': CALL('MERV - XMEV - GFGC230.AB - 24hs'),
                '240': CALL('MERV - XMEV - GFGC240.AB - 24hs'),
                '250': CALL('MERV - XMEV - GFGC250.AB - 24hs'),
                '260': CALL('MERV - XMEV - GFGC260.AB - 24hs'),
                '270': CALL('MERV - XMEV - GFGC270.AB - 24hs'),
                '280': CALL('MERV - XMEV - GFGC280.AB - 24hs'),
                '290': CALL('MERV - XMEV - GFGC290.AB - 24hs'),
                '300': CALL('MERV - XMEV - GFGC300.AB - 24hs'),
                '310': CALL('MERV - XMEV - GFGC310.AB - 24hs'),
                '320': CALL('MERV - XMEV - GFGC320.AB - 24hs'),
                '330': CALL('MERV - XMEV - GFGC330.AB - 24hs'),
                '340': CALL('MERV - XMEV - GFGC340.AB - 24hs'),
                '350': CALL('MERV - XMEV - GFGC350.AB - 24hs'),
                '360': CALL('MERV - XMEV - GFGC360.AB - 24hs')}
            },
        'put':{
            'FE':{
                '180': PUT('MERV - XMEV - GFGV180.FE - 24hs'),
                '185': PUT('MERV - XMEV - GFGV185.FE - 24hs'),
                '190': PUT('MERV - XMEV - GFGV190.FE - 24hs'),
                '195': PUT('MERV - XMEV - GFGV195.FE - 24hs'),
                '200': PUT('MERV - XMEV - GFGV200.FE - 24hs'),
                '210': PUT('MERV - XMEV - GFGV210.FE - 24hs'),
                '220': PUT('MERV - XMEV - GFGV220.FE - 24hs'),
                '230': PUT('MERV - XMEV - GFGV230.FE - 24hs'),
                '240': PUT('MERV - XMEV - GFGV240.FE - 24hs'),
                '250': PUT('MERV - XMEV - GFGV250.FE - 24hs'),
                '260': PUT('MERV - XMEV - GFGV260.FE - 24hs'),
                '270': PUT('MERV - XMEV - GFGV270.FE - 24hs'),
                '280': PUT('MERV - XMEV - GFGV280.FE - 24hs'),
                '290': PUT('MERV - XMEV - GFGV290.FE - 24hs'),
                '300': PUT('MERV - XMEV - GFGV300.FE - 24hs'),
                '310': PUT('MERV - XMEV - GFGV310.FE - 24hs'),
                '320': PUT('MERV - XMEV - GFGV320.FE - 24hs'),
                '330': PUT('MERV - XMEV - GFGV330.FE - 24hs'),
                '340': PUT('MERV - XMEV - GFGV340.FE - 24hs'),
                '350': PUT('MERV - XMEV - GFGV350.FE - 24hs'),
                '360': PUT('MERV - XMEV - GFGV360.FE - 24hs')},
            'AB':{
                '180': PUT('MERV - XMEV - GFGV180.AB - 24hs'),
                '185': PUT('MERV - XMEV - GFGV185.AB - 24hs'),
                '190': PUT('MERV - XMEV - GFGV190.AB - 24hs'),
                '195': PUT('MERV - XMEV - GFGV195.AB - 24hs'),
                '200': PUT('MERV - XMEV - GFGV200.AB - 24hs'),
                '210': PUT('MERV - XMEV - GFGV210.AB - 24hs'),
                '220': PUT('MERV - XMEV - GFGV220.AB - 24hs'),
                '230': PUT('MERV - XMEV - GFGV230.AB - 24hs'),
                '240': PUT('MERV - XMEV - GFGV240.AB - 24hs'),
                '250': PUT('MERV - XMEV - GFGV250.AB - 24hs'),
                '260': PUT('MERV - XMEV - GFGV260.AB - 24hs'),
                '270': PUT('MERV - XMEV - GFGV270.AB - 24hs'),
                '280': PUT('MERV - XMEV - GFGV280.AB - 24hs'),
                '290': PUT('MERV - XMEV - GFGV290.AB - 24hs'),
                '300': PUT('MERV - XMEV - GFGV300.AB - 24hs'),
                '310': PUT('MERV - XMEV - GFGV310.AB - 24hs'),
                '320': PUT('MERV - XMEV - GFGV320.AB - 24hs'),
                '330': PUT('MERV - XMEV - GFGV330.AB - 24hs'),
                '340': PUT('MERV - XMEV - GFGV340.AB - 24hs'),
                '350': PUT('MERV - XMEV - GFGV350.AB - 24hs'),
                '360': PUT('MERV - XMEV - GFGV360.AB - 24hs')}
            }},

    'duales':{
        '48':{
            'peso':{
                'al30':AL30('MERV - XMEV - AL30 - 48hs'),'gd30':GD30('MERV - XMEV - GD30 - 48hs'),
                'al35':AL35('MERV - XMEV - AL35 - 48hs'),'gd35':GD35('MERV - XMEV - GD35 - 48hs'),
                'ae38':AE38('MERV - XMEV - AE38 - 48hs'),'gd38':GD38('MERV - XMEV - GD38 - 48hs'),
                'al29':AL29('MERV - XMEV - AL29 - 48hs'),'gd29':GD29('MERV - XMEV - GD29 - 48hs'),
                'al41':AL41('MERV - XMEV - AL41 - 48hs'),'gd41':GD41('MERV - XMEV - GD41 - 48hs'),
                's31e2':S31E2('MERV - XMEV - S31E2 - 48hs'),'s28f2':S28F2('MERV - XMEV - S28F2 - 48hs'),
                's31m2':S31M2('MERV - XMEV - S31M2 - 48hs'),'s29a2':S29A2('MERV - XMEV - S29A2 - 48hs'),
                'aapl':AAPL('MERV - XMEV - AAPL - 48hs'),'ko':KO('MERV - XMEV - KO - 48hs')},
            'mep':{
                'al30':AL30('MERV - XMEV - AL30D - 48hs'),'gd30':GD30('MERV - XMEV - GD30D - 48hs'),
                'al35':AL35('MERV - XMEV - AL35D - 48hs'),'gd35':GD35('MERV - XMEV - GD35D - 48hs'),
                'ae38':AE38('MERV - XMEV - AE38D - 48hs'),'gd38':GD38('MERV - XMEV - GD38D - 48hs'),
                'al29':AL29('MERV - XMEV - AL29D - 48hs'),'gd29':GD29('MERV - XMEV - GD29D - 48hs'),
                'al41':AL41('MERV - XMEV - AL41D - 48hs'),'gd41':GD41('MERV - XMEV - GD41D - 48hs'),
                's31e2':S31E2('MERV - XMEV - SE2D - 48hs'),'s28f2':S28F2('MERV - XMEV - SF2D - 48hs'),
                's31m2':S31M2('MERV - XMEV - SM2D - 48hs'),'s29a2':S29A2('MERV - XMEV - SA2D - 48hs'),
                'aapl':AAPL('MERV - XMEV - AAPLD - 48hs'),'ko':KO('MERV - XMEV - KOD - 48hs')},
            'ccl':{
                'al30':AL30('MERV - XMEV - AL30C - 48hs'),'gd30':GD30('MERV - XMEV - GD30C - 48hs'),
                'al35':AL35('MERV - XMEV - AL35C - 48hs'),'gd35':GD35('MERV - XMEV - GD35C - 48hs'),
                'ae38':AE38('MERV - XMEV - AE38C - 48hs'),'gd38':GD38('MERV - XMEV - GD38C - 48hs'),
                'al29':AL29('MERV - XMEV - AL29C - 48hs'),'gd29':GD29('MERV - XMEV - GD29C - 48hs'),
                'al41':AL41('MERV - XMEV - AL41C - 48hs'),'gd41':GD41('MERV - XMEV - GD41C - 48hs'),
                's31e2':S31E2('MERV - XMEV - SE2C - 48hs'),'s28f2':S28F2('MERV - XMEV - SF2C - 48hs'),
                's31m2':S31M2('MERV - XMEV - SM2C - 48hs'),'s29a2':S29A2('MERV - XMEV - SA2C - 48hs'),
                'aapl':AAPL('MERV - XMEV - AAPLC - 48hs'),'ko':KO('MERV - XMEV - KOC - 48hs')}},
        '24':{
            'peso':{
                'al30':AL30('MERV - XMEV - AL30 - 24hs'),'gd30':GD30('MERV - XMEV - GD30 - 24hs'),
                'al35':AL35('MERV - XMEV - AL35 - 24hs'),'gd35':GD35('MERV - XMEV - GD35 - 24hs'),
                'ae38':AE38('MERV - XMEV - AE38 - 24hs'),'gd38':GD38('MERV - XMEV - GD38 - 24hs'),
                'al29':AL29('MERV - XMEV - AL29 - 24hs'),'gd29':GD29('MERV - XMEV - GD29 - 24hs'),
                'al41':AL41('MERV - XMEV - AL41 - 24hs'),'gd41':GD41('MERV - XMEV - GD41 - 24hs'),
                's31e2':S31E2('MERV - XMEV - S31E2 - 24hs'),'s28f2':S28F2('MERV - XMEV - S28F2 - 24hs'),
                's31m2':S31M2('MERV - XMEV - S31M2 - 24hs'),'s29a2':S29A2('MERV - XMEV - S29A2 - 24hs'),
                'aapl':AAPL('MERV - XMEV - AAPL - 24hs'),'ko':KO('MERV - XMEV - KO - 24hs')},
            'mep':{
                'al30':AL30('MERV - XMEV - AL30D - 24hs'),'gd30':GD30('MERV - XMEV - GD30D - 24hs'),
                'al35':AL35('MERV - XMEV - AL35D - 24hs'),'gd35':GD35('MERV - XMEV - GD35D - 24hs'),
                'ae38':AE38('MERV - XMEV - AE38D - 24hs'),'gd38':GD38('MERV - XMEV - GD38D - 24hs'),
                'al29':AL29('MERV - XMEV - AL29D - 24hs'),'gd29':GD29('MERV - XMEV - GD29D - 24hs'),
                'al41':AL41('MERV - XMEV - AL41D - 24hs'),'gd41':GD41('MERV - XMEV - GD41D - 24hs'),
                's31e2':S31E2('MERV - XMEV - SE2D - 24hs'),'s28f2':S28F2('MERV - XMEV - SF2D - 24hs'),
                's31m2':S31M2('MERV - XMEV - SM2D - 24hs'),'s29a2':S29A2('MERV - XMEV - SA2D - 24hs'),
                'aapl':AAPL('MERV - XMEV - AAPLD - 24hs'),'ko':KO('MERV - XMEV - KOD - 24hs')},
            'ccl':{
                'al30':AL30('MERV - XMEV - AL30C - 24hs'),'gd30':GD30('MERV - XMEV - GD30C - 24hs'),
                'al35':AL35('MERV - XMEV - AL35C - 24hs'),'gd35':GD35('MERV - XMEV - GD35C - 24hs'),
                'ae38':AE38('MERV - XMEV - AE38C - 24hs'),'gd38':GD38('MERV - XMEV - GD38C - 24hs'),
                'al29':AL29('MERV - XMEV - AL29C - 24hs'),'gd29':GD29('MERV - XMEV - GD29C - 24hs'),
                'al41':AL41('MERV - XMEV - AL41C - 24hs'),'gd41':GD41('MERV - XMEV - GD41C - 24hs'),
                's31e2':S31E2('MERV - XMEV - SE2C - 24hs'),'s28f2':S28F2('MERV - XMEV - SF2C - 24hs'),
                's31m2':S31M2('MERV - XMEV - SM2C - 24hs'),'s29a2':S29A2('MERV - XMEV - SA2C - 24hs'),
                'aapl':AAPL('MERV - XMEV - AAPLC - 24hs'),'ko':KO('MERV - XMEV - KOC - 24hs')}},
        'CI':{
            'peso':{
                'al30':AL30('MERV - XMEV - AL30 - CI'),'gd30':GD30('MERV - XMEV - GD30 - CI'),
                'al35':AL35('MERV - XMEV - AL35 - CI'),'gd35':GD35('MERV - XMEV - GD35 - CI'),
                'ae38':AE38('MERV - XMEV - AE38 - CI'),'gd38':GD38('MERV - XMEV - GD38 - CI'),
                'al29':AL29('MERV - XMEV - AL29 - CI'),'gd29':GD29('MERV - XMEV - GD29 - CI'),
                'al41':AL41('MERV - XMEV - AL41 - CI'),'gd41':GD41('MERV - XMEV - GD41 - CI'),
                's31e2':S31E2('MERV - XMEV - S31E2 - CI'),'s28f2':S28F2('MERV - XMEV - S28F2 - CI'),
                's31m2':S31M2('MERV - XMEV - S31M2 - CI'),'s29a2':S29A2('MERV - XMEV - S29A2 - CI'),
                'aapl':AAPL('MERV - XMEV - AAPL - CI'),'ko':KO('MERV - XMEV - KO - CI')},
            'mep':{
                'al30':AL30('MERV - XMEV - AL30D - CI'),'gd30':GD30('MERV - XMEV - GD30D - CI'),
                'al35':AL35('MERV - XMEV - AL35D - CI'),'gd35':GD35('MERV - XMEV - GD35D - CI'),
                'ae38':AE38('MERV - XMEV - AE38D - CI'),'gd38':GD38('MERV - XMEV - GD38D - CI'),
                'al29':AL29('MERV - XMEV - AL29D - CI'),'gd29':GD29('MERV - XMEV - GD29D - CI'),
                'al41':AL41('MERV - XMEV - AL41D - CI'),'gd41':GD41('MERV - XMEV - GD41D - CI'),
                's31e2':S31E2('MERV - XMEV - SE2D - CI'),'s28f2':S28F2('MERV - XMEV - SF2D - CI'),
                's31m2':S31M2('MERV - XMEV - SM2D - CI'),'s29a2':S29A2('MERV - XMEV - SA2D - CI'),
                'aapl':AAPL('MERV - XMEV - AAPLD - CI'),'ko':KO('MERV - XMEV - KOD - CI')},
            'ccl':{
                'al30':AL30('MERV - XMEV - AL30C - CI'),'gd30':GD30('MERV - XMEV - GD30C - CI'),
                'al35':AL35('MERV - XMEV - AL35C - CI'),'gd35':GD35('MERV - XMEV - GD35C - CI'),
                'ae38':AE38('MERV - XMEV - AE38C - CI'),'gd38':GD38('MERV - XMEV - GD38C - CI'),
                'al29':AL29('MERV - XMEV - AL29C - CI'),'gd29':GD29('MERV - XMEV - GD29C - CI'),
                'al41':AL41('MERV - XMEV - AL41C - CI'),'gd41':GD41('MERV - XMEV - GD41C - CI'),
                's31e2':S31E2('MERV - XMEV - SE2C - CI'),'s28f2':S28F2('MERV - XMEV - SF2C - CI'),
                's31m2':S31M2('MERV - XMEV - SM2C - CI'),'s29a2':S29A2('MERV - XMEV - SA2C - CI'),
                'aapl':AAPL('MERV - XMEV - AAPLC - CI'),'ko':KO('MERV - XMEV - KOC - CI')}}
            },

    'acciones':{
        '48':{
            'ggal': GGAL('MERV - XMEV - GGAL - 48hs'),
            'ypfd': YPFD('MERV - XMEV - YPFD - 24hs')},
        'CI':{
            'ggal': GGAL('MERV - XMEV - GGAL - CI'),
            'ypfd': YPFD('MERV - XMEV - YPFD - CI')}
            },
    }




