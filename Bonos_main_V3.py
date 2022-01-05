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
    global vendoA,comproB,vendoB,comproA,saldoA,saldoB
    if t1 == 's31e2':
        cantidad = ins['5'][1]
    else:
        cantidad = ins['1'][1]
    vendoA = round(((t1/100) * (1 - costos)) * cantidad,2)
    comproB = round(vendoA / ((t2/100) * (1 + costos)),0)
    vendoB = round(comproB * ((t3/100) * (1 - costos)),2)
    comproA = round(vendoA / ((t4/100) * (1 + costos)),0)

    saldoA = round(vendoA - comproB * (t2/100),2)
    saldoB = round(vendoB - comproA * (t4/100),2)
    print(time.strftime("%H:%M:%S"),f'  $:{vendoA}',end="  ")
    print(f'bon:{comproB}',end="  ")
    print(f'$:{vendoB}',end="  ")
    print(f'bon:{comproA}',end=" _ ") 

costos = 0.0026
limite = 1000
gana = round(0,0)
moneda1 = round(0,4)
moneda2 = round(0,4)

ins = {
    '1':['al30',100,'gd30'],    '2':['0',100,'al30'],
    '3':['0',100,'0'],    '4':['0',100,'0'],
    '5':['0',1000,'0'],  '6':['0',1000,'0']}

def vuelta(a,b,c,d):
    global limite,gana,moneda1,moneda2
    for i,e in ins.items():
        while e[0] != '0':
            t1 = a(e[0]).precio_BI()
            t2 = b(e[2]).precio_OF()
            t3 = c(e[2]).precio_BI()
            t4 = d(e[0]).precio_OF()
            if 2>1:#t1 != 1000 and t2 != 1000 and t3 != 1000 and t4 != 1000:
                cruce(t1,t2,t3,t4)
                if comproA < e[1]:# and cclCI(e[0]).cantidad_BI() > e[1] and cclCI(e[2]).cantidad_OF() >= comproCCL and mepCI(e[2]).cantidad_BI() >= comproCCL and mepCI(e[0]).cantidad_OF() >= comproMEP:

                    #vender(    a(e[0]),     e[1],       a(e[0]).precio_BI())
                    #comprar(   b(e[2]),     comproB,    b(e[2]).precio_OF())
                    #vender(    c(e[2]),     comproB,    c(e[2]).precio_BI())
                    #comprar(   d(e[0]),     comproA,    d(e[0]).precio_OF())

                    gana += comproA - e[1]
                    limite -= e[1]
                    moneda1 += saldoA
                    moneda2 += saldoB
                    print(f'{e[0]}/{e[2]}, bonos :{gana}, $ {moneda1} y $ {moneda2} _ limite:{limite}'),time.sleep(5)
                    continue
                else:
                    print(f'NO hay cruce entre {e[0]} _ {e[2]} _ limite: {limite}')
                    break
            else:
                print(time.strftime("%H:%M:%S"),f' Sin precios para {e[0]} _ {e[2]}')
                break


while limite > 0:
    if time.strftime("%H:%M:%S") <= '17:00:10':
        print('...................... MERCADO CERRADO 17HS .......................')
        break
    if time.strftime("%H:%M:%S") <= '15:59:15':
        print('CCL vs MEP_CI/', end ='  '), vuelta(cclCI,cclCI,mepCI,mepCI)
        print('MEP vs CCL_CI/', end ='  '), vuelta(mepCI,mepCI,cclCI,cclCI)

    else:
        print('CCL vs MEP_48/', end ='  '), vuelta(ccl48,ccl48,mep48,mep48)
        print('MEP vs CCL_48/', end ='  '), vuelta(mep48,mep48,ccl48,cclCI)
