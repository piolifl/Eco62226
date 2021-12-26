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
    for tipo, valor in ticker['bonos']['48']['peso'].items():
        if tipo == bono:
            return valor
def mep48(bono): 
    for tipo, valor in ticker['bonos']['48']['mep'].items():
        if tipo == bono:
            return valor
def ccl48(bono): 
    for tipo, valor in ticker['bonos']['48']['ccl'].items():
        if tipo == bono:
            return valor

def ccl_mep(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoMEP,comproMEP
    vendoCCL = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproCCL = round(vendoCCL / (t2/100),0)
    vendoMEP = round(comproCCL * ((t3/100)* (1-costos)),2)
    comproMEP = round(vendoMEP // (t4/100),0)
    print(f'venCCL: {vendoCCL}',end=" // ")
    print(f'bonosCCL: {comproCCL}',end=" // ")
    print(f'venMEP:{vendoMEP}',end=" // ")
    print(f'bonosMEP:{comproMEP}',end=" //// ")   
def mep_ccl(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoMEP,comproMEP
    vendoMEP = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproMEP = round(vendoMEP / (t2/100),0)
    vendoCCL = round(comproMEP * ((t3/100)* (1-costos)),2)
    comproCCL = round(vendoCCL // (t4/100),0)
    print(f'venMEP: {vendoMEP}',end=" // ")
    print(f'bonosMEP: {comproMEP}',end=" // ")
    print(f'venCCL:{vendoCCL}',end=" // ")
    print(f'bonosCCL:{comproCCL}',end=" //// ") 

costos = 0.0052
limite = 1000

ins = {
    '1':['al30',100,'gd30'],'2':['al30',100,'gd35'],'3':['al30',100,'al35'],
    '4':['gd30',100,'al30'],'5':['gd30',100,'gd35'],'6':['gd30',100,'al35'] }

while limite <= 1000:
    if time.strftime("%H:%M:%S") >= '17:00:10':
        print('...................... MERCADO CERRADO 17HS .......................')
        break
    for i, e in ins.items():
        while e[0] != '0':
            '''while True:
                if ccl48(e[0]).precio_BI() != 1000 and ccl48(e[2]).precio_OF() != 1000 and mep48(e[0]).precio_BI() != 1000 and mep48(e[2]).precio_OF() != 1000:
                    if ccl48(e[0]).cantidad_BI() > e[1] and ccl48(e[2]).cantidad_OF() >= comproCCL and mep48(e[2]).cantidad_BI() >= comproCCL and mep48(e[0]).cantidad_OF() >= comproMEP:
                        break
                    else:
                        print('No hay suficientes compradores/vendedores',time.strftime("%H:%M:%S")),time.sleep(1)
                else:
                    print('Esperando completar los precios ',time.strftime("%H:%M:%S")),time.sleep(2)'''
            ccl_mep(
                    ccl48(e[0]).precio_BI(),ccl48(e[2]).precio_OF(),
                    mep48(e[2]).precio_BI(),mep48(e[0]).precio_OF())

            if comproMEP > e[1]:

                #vender(ccl48(e[0]),e[1],ccl48(e[0]).precio_BI())
                #comprar(ccl48(e[2]),comproCCL,ccl48(e[2]).precio_OF())
                #vender(mep48(e[2]),comproCCL,mep48(e[2]).precio_BI())
                #comprar(mep48(e[0]),comproMEP,mep48(e[0]).precio_OF())

                print(f'Ratio positivo, sale ganando {comproMEP - e[1]}')
                limite -= e[1]
                break
            else:
                print(f'Sin posibles ratios entre {e[0]} y {e[2]} ',time.strftime("%H:%M:%S")),time.sleep(0)
                break
    
    for i, e in ins.items():
        while e[0] != '0':
            while True:
                if mep48(e[0]).precio_BI() != 1000 and mep48(e[2]).precio_OF() != 1000 and ccl48(e[0]).precio_BI() != 1000 and ccl48(e[2]).precio_OF() != 1000:
                    if mep48(e[0]).cantidad_BI() > e[1] and mep48(e[2]).cantidad_OF() >= comproMEP and ccl48(e[2]).cantidad_BI() >= comproMEP and ccl48(e[0]).cantidad_OF() >= comproCCL:
                        break
                    else:
                        print('No hay suficientes compradores/vendedores',time.strftime("%H:%M:%S")),time.sleep(1)
                else:
                    print('Esperando completar los precios ',time.strftime("%H:%M:%S")),time.sleep(2)
            mep_ccl(
                    mep48(e[0]).precio_BI(),mep48(e[2]).precio_OF(),
                    ccl48(e[2]).precio_BI(),ccl48(e[0]).precio_OF())

            if comproCCL > e[1]:

                #vender(mep48(e[0]),e[1],mep48(e[0]).precio_BI())
                #comprar(mep48(e[2]),comproMEP,mep48(e[2]).precio_OF())
                #vender(ccl48(e[2]),comproMEP,ccl48(e[2]).precio_BI())
                #comprar(ccl48(e[0]),comproCCL,ccl48(e[0]).precio_OF())

                print(f'Ratio positivo, sale ganando {comproCCL - e[1]}')
                limite -= e[1]
                break
            else:
                print(f'Sin posibles ratios entre {e[0]} y {e[2]} ',time.strftime("%H:%M:%S")),time.sleep(0)
                break
     
    