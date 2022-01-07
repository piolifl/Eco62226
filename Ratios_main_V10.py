from Operaciones_class import ticker
import pyRofex
import math
import time

def comprar(compra,cantidad, precio):
    pyRofex.send_order(ticker=compra, 
                        side=pyRofex.Side.BUY,
                        size = cantidad,   
                        price = precio,   
                        order_type=pyRofex.OrderType.LIMIT)
def vender(vendo,cantidad, precio):
    pyRofex.send_order(ticker=vendo, 
                        side=pyRofex.Side.SELL,
                        size = cantidad,   
                        price = precio,   
                        order_type=pyRofex.OrderType.LIMIT)

def strikeCall(base): 
    for baseOperada, valor in ticker['opciones']['call']['FE'].items():
        if baseOperada == base:
            return valor
def strikePut(base): 
    for baseOperada, valor in ticker['opciones']['put']['FE'].items():
        if baseOperada == base:
            return valor

costos = 0.0052

call = {
        '1': ['180',1, 27.3,'200',2, 14.21],
        '2': ['0',2, 26.55,'210',3, 15.65],
        '3': ['0', 2,  21.55,'0',  3,  14],
        '4': ['0', 2,  21.65,'0',  3,  12.2],
        '5': ['0', 2,  4.5,'0',  3,  2.55]
        }

while True:
    if time.strftime("%H:%M:%S") >= '17:00:10':
        print('...................... MERCADO CERRADO 17HS .......................')
        break
    for i, e in call.items():
        while e[0] != '0':
            ratioActual = round(strikeCall(e[0]).precio_BI()  / strikeCall(e[3]).precio_OF(),2)
            ratioEntrada = round(e[2]  / e[5] ,2)
            saldo = round(
                ((strikeCall(e[0]).precio_BI() * e[1] * 100 * (1 - costos)) - (e[2] * e[1] * 100) * (1 + costos)) -
                ((strikeCall(e[3]).precio_OF() * e[4] * 100 * (1 + costos)) - (e[5] * e[4] * 100)) * (1 - costos),2)
            
            if ratioActual > ratioEntrada * (1 + 0.15) and saldo > 100:

                if strikeCall(e[0]).precio_BI() != 1000 != strikeCall(e[3]).precio_OF():

                    if strikeCall(e[0]).cantidad_BI() >= e[1] and strikeCall(e[0]).cantidad_OF() >= e[4]:

                        print(f'CERRADO _ {e[0]}: {strikeCall(e[0]).precio_BI()} // {e[3]}: {strikeCall(e[3]).precio_OF()} RESULTADO: {saldo} ')

                        vender(strikeCall(e[0]),e[1],strikeCall(e[0]).precio_BI())
                        comprar(strikeCall(e[3]),e[4],strikeCall(e[3]).precio_OF())

                        e[0] = '0'
                        break
                    else:
                        print(f'NO hay compradores/vendedores {e[0]}/{e[3]} ',time.strftime("%H:%M:%S"))
                        break
                else:
                    print(f'Sin precios para {e[0]} o {e[3]} ',time.strftime("%H:%M:%S"))
                    break
            else:
                ggal = ticker['acciones']['48']['ggal'].precio_LA()
                print(time.strftime("%H:%M:%S"),f' GGAL:{ggal} _{e[0]}:{strikeCall(e[0]).precio_BI()} _{e[3]}:{strikeCall(e[3]).precio_OF()} _rEntrada:{ratioEntrada} _rActual:{ratioActual} //total:{saldo}')
                break
       
