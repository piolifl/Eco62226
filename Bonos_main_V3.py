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
def pes24(bono): 
    for tipo, valor in ticker['duales']['24']['peso'].items():
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
def mep24(bono): 
    for tipo, valor in ticker['duales']['24']['mep'].items():
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
def ccl24(bono): 
    for tipo, valor in ticker['duales']['24']['ccl'].items():
        if tipo == bono:
            return valor
def cclCI(bono): 
    for tipo, valor in ticker['duales']['CI']['ccl'].items():
        if tipo == bono:
            return valor


def cruce(t1,t2,t3,t4):
    global vendoA,comproB,vendoB,comproA,saldoA,saldoB,liquidoB, cant
    vendoA = round(((t1/100) * (1 - costos)) * cant,2)
    comproB = round(vendoA / ((t2/100) * (1 + costos)),0)
    liquidoB = round(t2/100 * comproB,0)
    vendoB = round(comproB * ((t3/100) * (1 - costos)),2)
    comproA = round(vendoB / ((t4/100) * (1 + costos)),0)
    saldoA = round(vendoA - comproB * (t2/100),2)
    saldoB = round(vendoB - comproA * (t4/100),2)
    print(time.strftime("%H:%M:%S"),f' $:{vendoA}',end="  ")
    print(f'bon:{comproB}',end="")
    print(f'(${liquidoB})',end="  ")
    print(f'$:{vendoB}',end="  ")
    print(f'FIN:{comproA}',end=" _ ") 

def vuelta(a,b,c,d):
    global limite,gana,moneda1,moneda2,moneda3
    for i,e in ins.items():
        cant = e[1]
        while e[0] != '0':
            t1 = a(e[0]).precio_BI()
            t2 = b(e[2]).precio_OF()
            t3 = c(e[2]).precio_BI()
            t4 = d(e[0]).precio_OF()
            cruce(t1,t2,t3,t4)
            if limite > 0:
                if t1 != 1000 and t2 != 1000 and t3 != 1000 and t4 != 1000:
                    if comproA > e[1] :
                        if a(e[0]).cantidad_BI() > e[1] and b(e[2]).cantidad_OF() >= comproB and c(e[2]).cantidad_BI() >= comproB and d(e[0]).cantidad_OF() >= comproA:

                            #vender(    a(e[0]),     e[1],       a(e[0]).precio_BI())
                            #comprar(   b(e[2]),     comproB,    b(e[2]).precio_OF())
                            #vender(    c(e[2]),     comproB,    c(e[2]).precio_BI())
                            #comprar(   d(e[0]),     comproA,    d(e[0]).precio_OF())

                            gana += comproA - e[1]
                            limite -= e[1]
                            moneda1 += round(saldoA,2)
                                 
                            if len(str(t3)) >= 4:
                                moneda3 += round(saldoB,2)
                                print(f'{e[0]}/{e[2]}, bonos:{gana} / u$d{moneda1} / u$d{moneda2} / Ars{moneda3} _ lim:{limite}')
                                continue
                            else:
                                moneda2 += round(saldoB,2)
                                print(f'{e[0]}/{e[2]}, bonos:{gana} / u$d{moneda1} / u$s{moneda2} / Ars{moneda3} _ lim:{limite}')
                                continue
                        else:
                            print(f' Sin bid/ask en {e[0]} _ {e[2]} _ limite:{limite}')
                            break
                    else:
                        print(f'//NO hay cruce {e[0]} _ {e[2]} _ limite:{limite}')
                        break
                else:
                    print(f' Sin precios para {e[0]} _ {e[2]} _ limite:{limite}')
                    break
            else:
                print(f' Limite = {limite} AGOTADO !!!')
                break


costos = 0.0026
limite = 100000
gana = round(0,0)
moneda1 = round(0,2)
moneda2 = round(0,2)
moneda3 = round(0,2)

ins = {
    '1':['al30',100,'gd30'],    '2':['gd30',100,'al30'],
    '3':['al30',100,'s31e2'],    '4':['gd30',100,'s31e2'],
    '5':['s31e2',1000,'al30'],  '6':['s31e2',1000,'gd30'],
    '7':['0',100,'gd29'],  '8':['0',100,'gd35'],
    '9':['0',100,'gd38'],  '10':['0',100,'gd41'],

    '11':['0',100,'al30'],  '12':['0',100,'s31e2'],
    '12':['0',100,'al29'],  '13':['0',100,'al35'],
    '14':['0',100,'ae38'],  '15':['0',100,'al41'],
    '16':['0',100,'gd29'],  '17':['0',100,'gd35'],
    '18':['0',100,'gd38'],  '19':['0',100,'gd41']
    }

cant = ins['1'][1]

while True:
    if time.strftime("%H:%M:%S") <= '11:00:05':
        print('Esperando apertura del mercado ... ',time.strftime("%H:%M:%S")),time.sleep(1)
        continue
    if time.strftime("%H:%M:%S") >= '16:59:50':
        print(f'... MERCADO CERRADO 17HS ... {limite} ... {moneda1} ... {moneda2} ... {moneda3} ...')
        break
    if time.strftime("%H:%M:%S") <= '15:59:15' and limite > 0:
        vuelta(cclCI,cclCI,mepCI,mepCI)
        vuelta(mepCI,mepCI,cclCI,cclCI)
        vuelta(cclCI,cclCI,pesCI,pesCI)
        vuelta(mepCI,mepCI,pesCI,pesCI)
    #else: break

    if limite > 0:
        vuelta(ccl48,ccl48,mep48,mep48)
        vuelta(mep48,mep48,ccl48,ccl48)
        vuelta(ccl48,ccl48,pes48,pes48)
        vuelta(mep48,mep48,pes48,pes48)

        vuelta(ccl24,ccl24,mep24,mep24)
        vuelta(mep24,mep24,ccl24,ccl24)
        vuelta(ccl24,ccl24,pes24,pes24)
        vuelta(mep24,mep24,pes24,pes24)

    else: break

