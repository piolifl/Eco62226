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

def pes48(bono): 
    for tipo, valor in ticker['duales']['48']['peso'].items():
        if tipo == bono:
            return valor
def pesCI(bono): 
    for tipo, valor in ticker['duales']['CI']['peso'].items():
        if tipo == bono:
            return valor
def mep48(bono): 
    for tipo, valor in ticker['duales']['48']['mep'].items():
        if tipo == bono:
            return valor
def mepCI(bono): 
    for tipo, valor in ticker['duales']['CI']['mep'].items():
        if tipo == bono:
            return valor
def ccl48(bono): 
    for tipo, valor in ticker['duales']['48']['ccl'].items():
        if tipo == bono:
            return valor
def cclCI(bono): 
    for tipo, valor in ticker['duales']['CI']['ccl'].items():
        if tipo == bono:
            return valor


def cruce(t1,t2,t3,t4):
    global vendoA,comproB,vendoB,comproA,saldoA,saldoB,liquidoB
    if t1 == 's31e2':
        cantidad = ins['5'][1]
    else:
        cantidad = ins['1'][1]
    vendoA = round(((t1/100) * (1 - costos)) * cantidad,2)
    comproB = round(vendoA / ((t2/100) * (1 + costos)),0)
    liquidoB = round(t2/100 * comproB,0)
    vendoB = round(comproB * ((t3/100) * (1 - costos)),2)
    comproA = round(vendoB / ((t4/100) * (1 + costos)),0)

    saldoA = round(vendoA - comproB * (t2/100),2)
    saldoB = round(vendoB - comproA * (t4/100),2)
    print(time.strftime("%H:%M:%S"),f'  $:{vendoA}',end="  ")
    print(f'bon:{comproB}',end="")
    print(f'(${liquidoB})',end="  ")
    print(f'$:{vendoB}',end="  ")
    print(f'bon:{comproA}',end=" _ ") 


def vuelta(a,b,c,d):
    global limite,gana,moneda1,moneda2
    for i,e in ins.items():
        while e[0] != '0':
            t1 = a(e[0]).precio_BI()
            t2 = b(e[2]).precio_OF()
            t3 = c(e[2]).precio_BI()
            t4 = d(e[0]).precio_OF()
            cruce(t1,t2,t3,t4)

            if limite > 0:

                if t1 != 1000 and t2 != 1000 and t3 != 1000 and t4 != 1000:

                    if comproA > e[1]:

                        if  a(e[0]).cantidad_BI() > e[1] and b(e[2]).cantidad_OF() >= comproB and c(e[2]).cantidad_BI() >= comproB and d(e[0]).cantidad_OF() >= comproA:

                            #vender(    a(e[0]),     e[1],       a(e[0]).precio_BI())
                            #comprar(   b(e[2]),     comproB,    b(e[2]).precio_OF())
                            #vender(    c(e[2]),     comproB,    c(e[2]).precio_BI())
                            #comprar(   d(e[0]),     comproA,    d(e[0]).precio_OF())

                            gana += comproA - e[1]
                            limite -= e[1]
                            moneda1 += round(saldoA,2)
                            moneda2 += round(saldoB,2)
                            print(f'{e[0]}/{e[2]}, bonos :{gana}, $ {moneda1} y $ {moneda2} _ limite:{limite}'),time.sleep(0)
                            continue
                        else:
                            print(f' Sin bid/ask en {e[0]} _ {e[2]} _ limite: {limite}')
                            break
                    else:
                        print(f' NO hay cruce entre {e[0]} _ {e[2]} _ limite: {limite}')
                        break
                else:
                    print(f' Sin precios para {e[0]} _ {e[2]} _ limite: {limite}')
                    break
            else:
                print(f' Limite = {limite} AGOTADO !!!')
                break


costos = 0.0026
limite = 100000
gana = round(0,0)
moneda1 = round(0,4)
moneda2 = round(0,4)

ins = {
    '1':['al30',100,'gd30'],    '2':['al30',100,'s31e2'],
    '3':['gd30',100,'s31e2'],    '4':['gd30',100,'al30'],
    '5':['s31e2',1000,'al30'],  '6':['s31e2',1000,'gd30']}


while True:
    if time.strftime("%H:%M:%S") >= '17:00:10':
        print('...................... MERCADO CERRADO 17HS .......................')
        break
    if time.strftime("%H:%M:%S") <= '15:59:15' and limite > 0:
        vuelta(cclCI,cclCI,mepCI,mepCI)
        vuelta(mepCI,mepCI,cclCI,cclCI)
        vuelta(cclCI,cclCI,pesCI,pesCI)
        vuelta(mepCI,mepCI,pesCI,pesCI)


    if limite > 0:
        vuelta(ccl48,ccl48,mep48,mep48)
        vuelta(mep48,mep48,ccl48,ccl48)
        vuelta(ccl48,ccl48,pes48,pes48)
        vuelta(mep48,mep48,pes48,pes48)
    else: break

