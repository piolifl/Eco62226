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
    print(time.strftime("%H:%M:%S"), f'CCL:{vendoCCL}',end="  ")
    print(f'bon:{comproCCL}',end="  ")
    print(f'MEP:{vendoMEP}',end="  ")
    print(f'bon:{comproMEP}',end="  ")   
def mep_ccl(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoMEP,comproMEP
    vendoMEP = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproMEP = round(vendoMEP / (t2/100),0)
    vendoCCL = round(comproMEP * ((t3/100)* (1-costos)),2)
    comproCCL = round(vendoCCL // (t4/100),0)
    print(time.strftime("%H:%M:%S"), f'MEP:{vendoMEP}',end="  ")
    print(f'bon:{comproMEP}',end="  ")
    print(f'CCL:{vendoCCL}',end="  ")
    print(f'bon:{comproCCL}',end="  ") 
def ccl_pes(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoPES,comproPES
    vendoCCL = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproCCL = round(vendoCCL / (t2/100),0)
    vendoPES = round(comproCCL * ((t3/100)* (1-costos)),2)
    comproPES = round(vendoPES // (t4/100),0)
    print(time.strftime("%H:%M:%S"), f'CCL:{vendoCCL}',end="  ")
    print(f'bon:{comproCCL}',end="  ")
    print(f'PES:{vendoPES}',end="  ")
    print(f'bon:{comproPES}',end="  ")
def mep_pes(t1,t2,t3,t4):
    global vendoPES,comproPES,vendoMEP,comproMEP
    vendoMEP = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproMEP = round(vendoMEP / (t2/100),0)
    vendoPES = round(comproMEP * ((t3/100)* (1-costos)),2)
    comproPES = round(vendoPES // (t4/100),0)
    print(time.strftime("%H:%M:%S"), f'MEP:{vendoMEP}',end="  ")
    print(f'bon:{comproMEP}',end="  ")
    print(f'PES:{vendoPES}',end="  ")
    print(f'bon:{comproPES}',end="  ") 

costos = 0.0052
limite = 400
gana = 0

ins = {
    '1':['al30',100,'gd30'],'2':['0',100,'gd35'],'3':['0',100,'al35'],
    '4':['gd30',100,'al30'],'5':['0',100,'gd35'],'6':['0',100,'al35'] }

while True:
    if time.strftime("%H:%M:%S") >= '17:00:10' or limite == 0:
        print('...................... MERCADO CERRADO 17HS .......................')
        break
    for i, e in ins.items():
        while e[0] != '0':

            ccl_mep( ccl48(e[0]).precio_BI(),ccl48(e[2]).precio_OF(),mep48(e[2]).precio_BI(),mep48(e[0]).precio_OF()) 
                      
            if comproMEP > e[1]:

                if ccl48(e[0]).precio_BI() != 1000 and ccl48(e[2]).precio_OF() != 1000 and mep48(e[0]).precio_BI() != 1000 and mep48(e[2]).precio_OF() != 1000:

                    if ccl48(e[0]).cantidad_BI() > e[1] and ccl48(e[2]).cantidad_OF() >= comproCCL and mep48(e[2]).cantidad_BI() >= comproCCL and mep48(e[0]).cantidad_OF() >= comproMEP:

                        #vender(ccl48(e[0]),e[1],ccl48(e[0]).precio_BI())
                        #comprar(ccl48(e[2]),comproCCL,ccl48(e[2]).precio_OF())
                        #vender(mep48(e[2]),comproCCL,mep48(e[2]).precio_BI())
                        #comprar(mep48(e[0]),comproMEP,mep48(e[0]).precio_OF())

                        gana += comproMEP - e[1]
                        limite -= e[1]
                        print(f'Limite:{limite}, Gana:{comproMEP - e[1]}, Total:{gana}')
                    else:
                        print('Sin compradores/vendedores CCL/MEP')
                else:
                    print('No hay precios CCL/MEP')
            else:
                print(f'Sin ratios {e[0]}.ccl / {e[2]}.mep ')


                mep_ccl(mep48(e[0]).precio_BI(),mep48(e[2]).precio_OF(),ccl48(e[2]).precio_BI(),ccl48(e[0]).precio_OF())

            if comproCCL > e[1]:

                if mep48(e[0]).precio_BI() != 1000 and mep48(e[2]).precio_OF() != 1000 and ccl48(e[0]).precio_BI() != 1000 and ccl48(e[2]).precio_OF() != 1000:

                    if mep48(e[0]).cantidad_BI() > e[1] and mep48(e[2]).cantidad_OF() >= comproMEP and ccl48(e[2]).cantidad_BI() >= comproMEP and ccl48(e[0]).cantidad_OF() >= comproCCL:

                        #vender(mep48(e[0]),e[1],mep48(e[0]).precio_BI())
                        #comprar(mep48(e[2]),comproMEP,mep48(e[2]).precio_OF())
                        #vender(ccl48(e[2]),comproMEP,ccl48(e[2]).precio_BI())
                        #comprar(ccl48(e[0]),comproCCL,ccl48(e[0]).precio_OF())

                        gana += comproCCL - e[1]
                        limite -= e[1]
                        print(f'Limite:{limite}, Gana:{comproCCL - e[1]}, Total:{gana}')
                    else:
                        print('Sin compradores/vendedores MEP/CCL')
                else:
                    print('No hay precios MEP/CCL ')
            else:
                print(f'Sin ratios {e[0]}.mep / {e[2]}.ccl ')

                ccl_pes(ccl48(e[0]).precio_BI(),ccl48(e[2]).precio_OF(),pes48(e[2]).precio_BI(),pes48(e[0]).precio_OF())

            if comproPES > e[1]:

                if ccl48(e[0]).precio_BI() != 1000 and ccl48(e[2]).precio_OF() != 1000 and pes48(e[0]).precio_BI() != 1000 and pes48(e[2]).precio_OF() != 1000:

                    if ccl48(e[0]).cantidad_BI() > e[1] and ccl48(e[2]).cantidad_OF() >= comproCCL and pes48(e[2]).cantidad_BI() >= comproCCL and pes48(e[0]).cantidad_OF() >= comproPES:

                        #vender(ccl48(e[0]),e[1],ccl48(e[0]).precio_BI())
                        #comprar(ccl48(e[2]),comproCCL,ccl48(e[2]).precio_OF())
                        #vender(pes48(e[2]),comproCCL,pes48(e[2]).precio_BI())
                        #comprar(pes48(e[0]),comproPES,pes48(e[0]).precio_OF())

                        gana += comproPES - e[1]
                        limite -= e[1]
                        print(f'Limite:{limite}, Gana:{comproPES - e[1]}, Total:{gana}')
                    else:
                        print('Sin compradores/vendedores CCL/PES')
                else:
                    print('No hay precios CCL/PES ')
            else:
                print(f'Sin ratios {e[0]}.ccl / {e[2]}.peso ')
                
                mep_pes(mep48(e[0]).precio_BI(),mep48(e[2]).precio_OF(),pes48(e[2]).precio_BI(),pes48(e[0]).precio_OF())

            if comproPES > e[1]:

                if mep48(e[0]).precio_BI() != 1000 and mep48(e[2]).precio_OF() != 1000 and pes48(e[0]).precio_BI() != 1000 and pes48(e[2]).precio_OF() != 1000:

                    if mep48(e[0]).cantidad_BI() > e[1] and mep48(e[2]).cantidad_OF() >= comproCCL and pes48(e[2]).cantidad_BI() >= comproCCL and pes48(e[0]).cantidad_OF() >= comproPES:

                        #vender(mep48(e[0]),e[1],mep48(e[0]).precio_BI())
                        #comprar(mep48(e[2]),comproMEP,mep48(e[2]).precio_OF())
                        #vender(pes48(e[2]),comproMEP,pes48(e[2]).precio_BI())
                        #comprar(pes48(e[0]),comproPES,pes48(e[0]).precio_OF())

                        gana += comproPES - e[1]
                        limite -= e[1]
                        print(f'Limite:{limite}, Gana:{comproPES - e[1]}, Total:{gana}')
                        break
                    else:
                        print('Sin compradores/vendedores CCL/PES')
                        break
                else:
                    print('No hay precios CCL/PES ')
                    break
            else:
                print(f'Sin ratios {e[0]}.ccl / {e[2]}.peso ')
                break
