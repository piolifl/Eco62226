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
    print(f'vendoCCL: {vendoCCL} ccl',end=" // ")
    print(f'comproCCL: {comproCCL} bonos ',end=" // ")
    print(f'vendoMEP:{vendoMEP} mep ',end=" /// ")
    print(f'comproMEP:{comproMEP}')   
def mep_ccl(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoMEP,comproMEP
    vendoMEP = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproMEP = round(vendoMEP / (t2/100),0)
    vendoCCL = round(comproMEP * ((t3/100)* (1-costos)),2)
    comproCCL = round(vendoCCL // (t4/100),0)
    print(f'vendoMEP: {vendoMEP} ccl',end=" // ")
    print(f'comproMEP: {comproMEP} bonos ',end=" // ")
    print(f'vendoCCL:{vendoCCL} mep ',end=" /// ")
    print(f'comproCCL:{comproCCL}')    


costos = 0.0052
limite = 1000

ins = {
    '1':['al30',100,'gd30'],'2':['al30',100,'gd35'],'3':['al30',100,'al35'],
    '4':['gd30',100,'al30'],'5':['gd30',100,'gd35'],'6':['gd30',100,'al35'] }

while True:
    for i, e in ins.items():
        while e[0] != '0':
            while True:
                if ccl48(e[0]).precio_BI() != 1000 and ccl48(e[2]).precio_OF() != 1000 and mep48(e[0]).precio_BI() != 1000 and mep48(e[2]).precio_OF() != 1000:
                    break
                else:
                    print('Esperando completar los precios ',time.strftime("%H:%M:%S")),time.sleep(2)
            ccl_mep(
                    ccl48(e[0]).precio_BI(),ccl48(e[2]).precio_OF(),
                    mep48(e[2]).precio_BI(),mep48(e[0]).precio_OF())

            if comproMEP > e[1]:

                if ccl48(e[0]).cantidad_BI() > e[1] and ccl48(e[2]).cantidad_OF() >= comproCCL and mep48(e[2]).cantidad_BI() >= comproCCL and mep48(e[0]).cantidad_OF() >= comproMEP :

                    print(f'Ratio positivo, sale ganando {comproMEP - e[1]}')
                    break
                else:
                    print('No hay suficientes compradores/vendedores',time.strftime("%H:%M:%S")),time.sleep(1)
                    break
            else:
                print(f'Sin ratios posibles {e[0]} / {e[2]} ',time.strftime("%H:%M:%S")),time.sleep(1)
                break
    
    for i, e in ins.items():
        while e[0] != '0':
            while True:
                if mep48(e[0]).precio_BI() != 1000 and mep48(e[2]).precio_OF() != 1000 and ccl48(e[0]).precio_BI() != 1000 and ccl48(e[2]).precio_OF() != 1000:
                    break
                else:
                    print('Esperando completar los precios ',time.strftime("%H:%M:%S")),time.sleep(2)
            mep_ccl(
                    mep48(e[0]).precio_BI(),mep48(e[2]).precio_OF(),
                    ccl48(e[2]).precio_BI(),ccl48(e[0]).precio_OF())

            if comproCCL > e[1]:

                if mep48(e[0]).cantidad_BI() > e[1] and mep48(e[2]).cantidad_OF() >= comproMEP and ccl48(e[2]).cantidad_BI() >= comproMEP and ccl48(e[0]).cantidad_OF() >= comproCCL :

                    print(f'Ratio positivo, sale ganando {comproCCL - e[1]}')
                    break
                else:
                    print('No hay suficientes compradores/vendedores',time.strftime("%H:%M:%S")),time.sleep(1)
                    break
            else:
                print(f'Sin ratios posibles {e[0]} / {e[2]} ',time.strftime("%H:%M:%S")),time.sleep(1)
                break

    print()
       
    