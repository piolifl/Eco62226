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
        '1': ['185',2, 24,'210',4, 12.5],
        '2': ['195', 2,  21.55,'210',  3,  14],
        '3': ['0', 1,  21,'0',  5,  13.95],
        '4': ['250', 2,  4.5,'270',  3,  2.55]
        }

while True:
    if time.strftime("%H:%M:%S") >= '17:00:10':
        print('...................... MERCADO CERRADO 17HS .......................')
        break
    for i, e in call.items():
        while e[0] != '0':
            while True:
                if strikeCall(e[0]).precio_BI() != 1000 != strikeCall(e[3]).precio_OF():
                    if strikeCall(e[0]).cantidad_BI() >= e[1] and strikeCall(e[0]).cantidad_OF() >= e[4]:
                        break
                    else:
                        print('Esperando compradores/vendedores ',time.strftime("%H:%M:%S")),time.sleep(1)
                else:
                    print('Esperando completar los precios ',time.strftime("%H:%M:%S")),time.sleep(1)

            ratioActual = round(strikeCall(e[0]).precio_BI()  / strikeCall(e[3]).precio_OF(),2)
            ratioEntrada = round(e[2]  / e[5] ,2)
            saldo = round(
                ((strikeCall(e[0]).precio_BI() * e[1] * 100 * (1 - costos)) - (e[2] * e[1] * 100) * (1 + costos)) -
                ((strikeCall(e[3]).precio_OF() * e[4] * 100 * (1 + costos)) - (e[5] * e[4] * 100)) * (1 - costos),2)
            
            if ratioActual > ratioEntrada * (1 + 0.15) and saldo > 100:

                print(f'CERRADO bull CALL: {e[0]} = {strikeCall(e[0]).precio_BI()}  // {e[3]} = {strikeCall(e[3]).precio_OF()} RESULT = {saldo} ')

                #vender(strikeCall(e[0]),e[1],strikeCall(e[0]).precio_BI())
                #comprar(strikeCall(e[3]),e[4],strikeCall(e[3]).precio_OF())

                e[0] = '0'

            else:
                ggal = ticker['acciones']['48']['ggal'].precio_LA()
                print(f'GGAL: {ggal} - bull CALL: {e[0]} = {strikeCall(e[0]).precio_BI()}  // {e[3]} = {strikeCall(e[3]).precio_OF()} da ratioEntrada:{ratioEntrada} /// ratioActual {ratioActual} = {saldo} /// ',time.strftime("%H:%M:%S")),time.sleep(1)
                break
       
