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
    global vendoA,comproB,vendoB,comproA,saldoA,saldoB
    if name1 == 'aapl' or name1 == 'ko':
        vendoA = round(((t1) * (1 - costos)) * cant,2)
        comproB = vendoA // ((t2/100) * (1 + costos))
        vendoB = round(comproB * ((t3/100) * (1 - costos)),2)
        comproA = vendoB // ((t4) * (1 + costos))
        saldoA = round(vendoA - comproB * (t2/100),2)
        saldoB = round(vendoB - comproA * (t4),2)
        #print(time.strftime("%H:%M:%S"),f'[I gana:{comproA}]',end="  ")
        print(time.strftime("%H:%M:%S"),'  I',end="  ")
    elif name2 == 'aapl' or name2 == 'ko':
        vendoA = round(((t1/100) * (1 - costos)) * cant,2)
        comproB = vendoA // ((t2) * (1 + costos))
        vendoB = round(comproB * ((t3) * (1 - costos)),2)
        comproA = vendoB // ((t4/100) * (1 + costos))
        saldoA = round(vendoA - comproB * (t2),2)
        saldoB = round(vendoB - comproA * (t4/100),2)
        #print(time.strftime("%H:%M:%S"),f'[II gana:{comproA}]',end="  ")
        print(time.strftime("%H:%M:%S"),' II',end="  ")
    else:
        vendoA = round(((t1/100) * (1 - costos)) * cant,2)
        comproB = vendoA // ((t2/100) * (1 + costos))
        vendoB = round(comproB * ((t3/100) * (1 - costos)),2)
        comproA = vendoB // ((t4/100) * (1 + costos))
        saldoA = round(vendoA - comproB * (t2/100),2)
        saldoB = round(vendoB - comproA * (t4/100),2)
        #print(time.strftime("%H:%M:%S"),f'[III gana:{comproA}]',end="  ")
        print(time.strftime("%H:%M:%S"),'III',end="  ")

def vuelta(a,b,c,d):
    global limite,ganaAL30,ganaGD30,ganaAAPL,ganaS31E2,moneda1,moneda2,moneda3,name1,name2,cant
    for i,e in ins.items():
        cant = e[1]
        name1 = e[0]
        name2 = e[2]
        while e[0] != '0':
            t1 = a(e[0]).precio_BI()
            t2 = b(e[2]).precio_OF()
            t3 = c(e[2]).precio_BI()
            t4 = d(e[0]).precio_OF()

            if t1 == 1000 and t2 == 1000 and t3 == 1000 and t4 == 1000:
                print(time.strftime("%H:%M:%S"),f'Faltan precios para {e[0]} {e[2]} [AL30:{ganaAL30} / GD30:{ganaGD30} / AAPL:{ganaAAPL} / S31E2:{ganaS31E2}] / u$d {round(moneda1,2)} / u$d {round(moneda2,2)} / Ars {round(moneda3,2)}')
                break
            else:
                cruce(t1,t2,t3,t4)
                if limite > 0:
                    if comproA > e[1] :
                        if a(e[0]).cantidad_BI() > e[1] and b(e[2]).cantidad_OF() >= comproB and c(e[2]).cantidad_BI() >= comproB and d(e[0]).cantidad_OF() >= comproA:

                            #vender(    a(e[0]),     e[1],       a(e[0]).precio_BI())
                            #comprar(   b(e[2]),     comproB,    b(e[2]).precio_OF())
                            #vender(    c(e[2]),     comproB,    c(e[2]).precio_BI())
                            #comprar(   d(e[0]),     comproA,    d(e[0]).precio_OF())

                            if e[0] == 'al30' or e[2] == 'al30':
                                ganaAL30 += comproA - e[1]
                                limite -= e[1]
                            elif e[0] == 'gd30':
                                ganaGD30 += comproA - e[1]
                            elif e[0] == 'aapl':
                                ganaAAPL += comproA - e[1]
                            elif e[0] == 's31e2':
                                ganaS31E2 += comproA - e[1]
                                    
                            moneda1 += saldoA

                            if len(str(t3)) >= 4:
                                moneda3 += saldoB
                                print(f'{e[0].upper()}__{e[2].upper()},  [AL30:{ganaAL30} / GD30:{ganaGD30} / AAPL:{ganaAAPL} / S31E2:{ganaS31E2}] / u$d {round(moneda1,2)} / u$d {round(moneda2,2)} / Ars {round(moneda3,2)} _ L:{limite}')
                                continue
                            else:
                                moneda2 += saldoB
                                print(f'{e[0].upper()}__{e[2].upper()},  [AL30:{ganaAL30} / GD30:{ganaGD30} / AAPL:{ganaAAPL} / S31E2:{ganaS31E2}] / u$d:{round(moneda1,2)} / u$s:{round(moneda2,2)} / Ars:{round(moneda3,2)} _ L:{limite}')
                                continue
                        else:
                            print(f'sin bid_ask {e[0].upper()}__{e[2]},  [AL30:{ganaAL30} / GD30:{ganaGD30} / AAPL:{ganaAAPL} / S31E2:{ganaS31E2}] / u$d {round(moneda1,2)} / u$d {round(moneda2,2)} / Ars {round(moneda3,2)} _ L:{limite}')
                            break
                    else:
                        print(f'no {e[0].upper()}__{e[2].upper()},  [AL30:{ganaAL30} / GD30:{ganaGD30} / AAPL:{ganaAAPL} / S31E2:{ganaS31E2}] / u$d {round(moneda1,2)} / u$d {round(moneda2,2)} / Ars {round(moneda3,2)} _ L:{limite}')
                        break
                else:
                    print(f'Limite {limite} AGOTADO!!! [AL30:{ganaAL30} / GD30:{ganaGD30} / AAPL:{ganaAAPL} / S31E2:{ganaS31E2}] / u$d {round(moneda1,2)} / u$d {round(moneda2,2)} / Ars {round(moneda3,2)}')
                    break

costos = 0.0026
limite = 100000
ganaAL30 = 0
ganaGD30 = 0
ganaAAPL = 0
ganaS31E2 = 0
moneda1 = 0
moneda2 = 0
moneda3 = 0

ins = {
    '1':['al30',175,'gd30'],'2':['al30',175,'gd35'],'3':['al30',175,'gd38'],'4':['al30',175,'s31e2'],'5':['al30',175,'s28f2'],'6':['al30',175,'aapl'],'7':['al30',175,'ko'],

    '10':['gd30',160,'al30'],'11':['gd30',160,'gd35'],'12':['gd30',160,'gd38'],'13':['gd30',160,'s31e2'],'14':['gd30',160,'s28f2'],'15':['gd30',160,'aapl'],'16':['gd30',160,'ko'],

    '20':['s31e2',6500,'al30'], '21':['s31e2',6500,'gd30'],'22':['s31e2',6500,'s28f2'],'23':['s31e2',6500,'aapl'],'24':['s31e2',6500,'ko'],

    '30':['s28f2',7650,'al30'], '31':['s28f2',7650,'gd30'],'32':['s28f2',7650,'s31e2'],'33':['s28f2',7650,'aapl'],'34':['s28f2',7650,'ko'],

    '40':['aapl',2,'al30'], '41':['aapl',2,'gd30'],'42':['aapl',2,'ko'],'43':['aapl',2,'s31e2'],'44':['aapl',2,'s28f2'],

    '50':['ko',3,'al30'], '51':['ko',3,'gd30'],'52':['ko',3,'aapl'],'53':['ko',3,'s31e2'],'54':['ko',3,'s28f2']
    }


while True:
    if time.strftime("%H:%M:%S") < '11:00:05':
        print('Esperando apertura del mercado ... ',time.strftime("%H:%M:%S")),time.sleep(1)
        continue
    elif time.strftime("%H:%M:%S") > '16:59:45':
        print(f'... MERCADO CERRADO 17HS ... Limite {limite} bonos ganados:{ganaAL30} / u$d:{round(moneda1,2)} / u$d:{round(moneda2,2)} / Ars:{round(moneda3,2)}')
        break
    if time.strftime("%H:%M:%S") < '15:59:30' and limite > 0:
        vuelta(cclCI,cclCI,mepCI,mepCI)
        vuelta(mepCI,mepCI,cclCI,cclCI)
        vuelta(cclCI,cclCI,pesCI,pesCI)
        vuelta(mepCI,mepCI,pesCI,pesCI)
    else: break

    if limite > 0:
        vuelta(ccl48,ccl48,mep48,mep48)
        vuelta(mep48,mep48,ccl48,ccl48)
        vuelta(ccl48,ccl48,pes48,pes48)
        vuelta(mep48,mep48,pes48,pes48)
    else: break

    if limite > 0:
        vuelta(ccl24,ccl24,mep24,mep24)
        vuelta(mep24,mep24,ccl24,ccl24)
        vuelta(ccl24,ccl24,pes24,pes24)
        vuelta(mep24,mep24,pes24,pes24)

    else: break

