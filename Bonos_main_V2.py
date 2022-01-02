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

def ccl_mep(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoMEP,comproMEP,saldoCCL,saldoMEP
    vendoCCL = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproCCL = round(vendoCCL / (t2/100),0)
    vendoMEP = round(comproCCL * ((t3/100)* (1-costos)),2)
    comproMEP = round(vendoMEP // (t4/100),0)
    saldoCCL = round(vendoCCL - comproCCL * (t2/100),2)
    saldoMEP = round(vendoMEP - comproMEP * (t3/100),2)
    print(time.strftime("%H:%M:%S"),f' __  CCL:{vendoCCL}',end="  ")
    print(f'bon:{comproCCL}',end="  ")
    print(f'MEP:{vendoMEP}',end="  ")
    print(f'bon:{comproMEP}',end="  __  ")
def mep_ccl(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoMEP,comproMEP,saldoMEP,saldoCCL
    vendoMEP = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproMEP = round(vendoMEP / (t2/100),0)
    vendoCCL = round(comproMEP * ((t3/100)* (1-costos)),2)
    comproCCL = round(vendoCCL // (t4/100),0)
    saldoMEP = round(vendoMEP - comproMEP * (t3/100),2)
    saldoCCL = round(vendoCCL - comproCCL * (t2/100),2)
    print(time.strftime("%H:%M:%S"),f' __  MEP:{vendoMEP}',end="  ")
    print(f'bon:{comproMEP}',end="  ")
    print(f'CCL:{vendoCCL}',end="  ")
    print(f'bon:{comproCCL}',end="  __  ")
def ccl_pes(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoPES,comproPES,saldoCCL, saldoPES
    vendoCCL = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproCCL = round(vendoCCL / (t2/100),0)
    vendoPES = round(comproCCL * ((t3/100)* (1-costos)),2)
    comproPES = round(vendoPES // (t4/100),0)
    saldoCCL = round(vendoCCL - comproCCL * (t2/100),2)
    saldoPES = round(vendoPES - comproPES * (t2/100),2)
    print(time.strftime("%H:%M:%S"),f' __  CCL:{vendoCCL}',end="  ")
    print(f'bon:{comproCCL}',end="  ")
    print(f'PES:{vendoPES}',end="  ")
    print(f'bon:{comproPES}',end="  __  ")
def mep_pes(t1,t2,t3,t4):
    global vendoPES,comproPES,vendoMEP,comproMEP,saldoMEP,saldoPES
    vendoMEP = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproMEP = round(vendoMEP / (t2/100),0)
    vendoPES = round(comproMEP * ((t3/100)* (1-costos)),2)
    comproPES = round(vendoPES // (t4/100),0)
    saldoMEP = round(vendoMEP - comproMEP * (t2/100),2)
    saldoPES = round(vendoPES - comproPES * (t2/100),2)
    print(time.strftime("%H:%M:%S"),f' __  MEP:{vendoMEP}',end="  ")
    print(f'bon:{comproMEP}',end="  ")
    print(f'PES:{vendoPES}',end="  ")
    print(f'bon:{comproPES}',end="  __  ") 

costos = 0.0052
limite = 1000
gana = round(0,0)
ccl = round(0,4)
mep = round(0,4)
peso = round(0,4)

ins = {
    '1':['al30',100,'gd30'],'2':['al30',100,'s31e2'],
    '3':['gd30',100,'al30'],'4':['gd30',100,'s31e2'],
    '5':['s31e2',1000,'al30'],'6':['s31e2',1000,'gd30']}

while limite > 0:
    if time.strftime("%H:%M:%S") >= '17:00:10':
        print('...................... MERCADO CERRADO 17HS .......................')
        break
    for i, e in ins.items():
        while e[0] != '0':
            if time.strftime("%H:%M:%S") >= '15:59:15':
                if limite > 0 and cclCI(e[0]).precio_BI() != 1000 and cclCI(e[2]).precio_OF() != 1000 and mepCI(e[0]).precio_BI() != 1000 and mepCI(e[2]).precio_OF() != 1000:
                    while True:
                        ccl_mep(cclCI(e[0]).precio_BI(),cclCI(e[2]).precio_OF(),mepCI(e[2]).precio_BI(),mepCI(e[0]).precio_OF())
                        if comproMEP >= e[1] and cclCI(e[0]).cantidad_BI() > e[1] and cclCI(e[2]).cantidad_OF() >= comproCCL and mepCI(e[2]).cantidad_BI() >= comproCCL and mepCI(e[0]).cantidad_OF() >= comproMEP:

                            #vender(cclCI(e[0]),e[1],cclCI(e[0]).precio_BI())
                            #comprar(cclCI(e[2]),comproCCL,cclCI(e[2]).precio_OF())
                            #vender(mepCI(e[2]),comproCCL,mepCI(e[2]).precio_BI())
                            #comprar(mepCI(e[0]),comproMEP,mepCI(e[0]).precio_OF())

                            gana += comproMEP - e[1]
                            limite -= e[1]
                            print(f'{e[0]}/{e[2]} /CI/ Total bonos:{gana}, total CCL: {saldoCCL}, total MEP {saldoMEP}')
                            continue
                        else:
                            print(f'NO hay /CI/ {e[0]}.ccl _ {e[2]}.mep _ LIM: {limite}')
                            break
                else:
                    print(f'Limite actual:{limite} Sin precios CI {e[0]}.ccl _ {e[2]}.mep')

                if limite > 0 and mepCI(e[0]).precio_BI() != 1000 and mepCI(e[2]).precio_OF() != 1000 and cclCI(e[0]).precio_BI() != 1000 and cclCI(e[2]).precio_OF() != 1000:
                    while True:
                        mep_ccl(mepCI(e[0]).precio_BI(),mepCI(e[2]).precio_OF(),cclCI(e[2]).precio_BI(),cclCI(e[0]).precio_OF())
                        if comproCCL >= e[1] and mepCI(e[0]).cantidad_BI() > e[1] and mepCI(e[2]).cantidad_OF() >= comproMEP and cclCI(e[2]).cantidad_BI() >= comproMEP and cclCI(e[0]).cantidad_OF() >= comproCCL:

                            #vender(mepCI(e[0]),e[1],mepCI(e[0]).precio_BI())
                            #comprar(mepCI(e[2]),comproMEP,mepCI(e[2]).precio_OF())
                            #vender(cclCI(e[2]),comproMEP,cclCI(e[2]).precio_BI())
                            #comprar(cclCI(e[0]),comproCCL,cclCI(e[0]).precio_OF())

                            gana += comproCCL - e[1]
                            limite -= e[1]
                            print(f'{e[0]}/{e[2]} /CI/ Total bonos:{gana}, total MEP: {saldoMEP}, total CCL {saldoCCL}')
                            continue
                        else:
                            print(f'NO hay /CI/ {e[0]}.mep _ {e[2]}.ccl _ LIM: {limite}')
                            break
                else:
                    print(f'Limite actual:{limite} Sin precios CI {e[0]}.mep _ {e[2]}.ccl')
                    
                '''if limite > 0 and cclCI(e[0]).precio_BI() != 1000 and cclCI(e[2]).precio_OF() != 1000 and pesCI(e[0]).precio_BI() != 1000 and pesCI(e[2]).precio_OF() != 1000:
                    while True:
                        ccl_pes(cclCI(e[0]).precio_BI(),cclCI(e[2]).precio_OF(),pesCI(e[2]).precio_BI(),pesCI(e[0]).precio_OF())
                        if comproPES >= e[1] and cclCI(e[0]).cantidad_BI() > e[1] and cclCI(e[2]).cantidad_OF() >= comproCCL and pesCI(e[2]).cantidad_BI() >= comproCCL and pesCI(e[0]).cantidad_OF() >= comproPES:

                            #vender(cclCI(e[0]),e[1],cclCI(e[0]).precio_BI())
                            #comprar(cclCI(e[2]),comproCCL,cclCI(e[2]).precio_OF())
                            #vender(pesCI(e[2]),comproCCL,pesCI(e[2]).precio_BI())
                            #comprar(pesCI(e[0]),comproPES,pesCI(e[0]).precio_OF())

                            gana += comproPES - e[1]
                            limite -= e[1]
                            print(f'{e[0]}/{e[2]} /CI/ Total bonos:{gana}, total CCL: {saldoCCL}, total PESO {saldoPES}')
                            continue
                        else:
                            print(f'NO hay /CI/ {e[0]}.ccl _ {e[2]}.peso _ LIM: {limite}')
                            break
                else:
                    print(f'Limite actual:{limite} Sin precios CI {e[0]}.ccl _ {e[2]}.peso')
                
                if limite > 0 and mepCI(e[0]).precio_BI() != 1000 and mepCI(e[2]).precio_OF() != 1000 and pesCI(e[0]).precio_BI() != 1000 and pesCI(e[2]).precio_OF() != 1000:
                    while True:
                        mep_pes(mepCI(e[0]).precio_BI(),mepCI(e[2]).precio_OF(),pesCI(e[2]).precio_BI(),pesCI(e[0]).precio_OF())
                        if comproPES >= e[1] and mepCI(e[0]).cantidad_BI() > e[1] and mepCI(e[2]).cantidad_OF() >= comproCCL and pesCI(e[2]).cantidad_BI() >= comproCCL and pesCI(e[0]).cantidad_OF() >= comproPES:

                            #vender(mepCI(e[0]),e[1],mepCI(e[0]).precio_BI())
                            #comprar(mepCI(e[2]),comproMEP,mepCI(e[2]).precio_OF())
                            #vender(pesCI(e[2]),comproMEP,pesCI(e[2]).precio_BI())
                            #comprar(pesCI(e[0]),comproPES,pesCI(e[0]).precio_OF())

                            gana += comproPES - e[1]
                            limite -= e[1]
                            print(f'{e[0]}/{e[2]} /CI/ Total bonos:{gana}, total MEP: {saldoMEP}, total PESO {saldoPES}')
                            continue
                        else:
                            print(f'NO hay /CI/ {e[0]}.mep _ {e[2]}.peso _ LIM: {limite}')
                            break
                else:
                    print(f'Limite actual:{limite} Sin precios CI {e[0]}.mep _ {e[2]}.peso')'''
            #else:
                #print('Cierran cortos ... continuan solo largos')

            
            if limite > 0 and ccl48(e[0]).precio_BI() != 1000 and ccl48(e[2]).precio_OF() != 1000 and mep48(e[0]).precio_BI() != 1000 and mep48(e[2]).precio_OF() != 1000:
                while True:
                    ccl_mep( ccl48(e[0]).precio_BI(),ccl48(e[2]).precio_OF(),mep48(e[2]).precio_BI(),mep48(e[0]).precio_OF())
                    if comproMEP >= e[1] and ccl48(e[0]).cantidad_BI() > e[1] and ccl48(e[2]).cantidad_OF() >= comproCCL and mep48(e[2]).cantidad_BI() >= comproCCL and mep48(e[0]).cantidad_OF() >= comproMEP:

                        #vender(ccl48(e[0]),e[1],ccl48(e[0]).precio_BI())
                        #comprar(ccl48(e[2]),comproCCL,ccl48(e[2]).precio_OF())
                        #vender(mep48(e[2]),comproCCL,mep48(e[2]).precio_BI())
                        #comprar(mep48(e[0]),comproMEP,mep48(e[0]).precio_OF())

                        gana += comproMEP - e[1]
                        limite -= e[1]
                        print(f'{e[0]}/{e[2]} /48/ Total bonos:{gana}, total CCL: {saldoCCL}, total MEP {saldoMEP}')
                        continue
                    else:
                        print(f'NO hay /48/ {e[0]}.ccl _ {e[2]}.mep _ LIM: {limite}')
                        break
            else:
                print(f'Limite actual:{limite} Sin precios 48 {e[0]}.ccl _ {e[2]}.mep')
                

            if limite > 0 and mep48(e[0]).precio_BI() != 1000 and mep48(e[2]).precio_OF() != 1000 and ccl48(e[0]).precio_BI() != 1000 and ccl48(e[2]).precio_OF() != 1000:
                while True:
                    mep_ccl(mep48(e[0]).precio_BI(),mep48(e[2]).precio_OF(),ccl48(e[2]).precio_BI(),ccl48(e[0]).precio_OF())
                    if comproCCL >= e[1] and mep48(e[0]).cantidad_BI() > e[1] and mep48(e[2]).cantidad_OF() >= comproMEP and ccl48(e[2]).cantidad_BI() >= comproMEP and ccl48(e[0]).cantidad_OF() >= comproCCL:

                        #vender(mep48(e[0]),e[1],mep48(e[0]).precio_BI())
                        #comprar(mep48(e[2]),comproMEP,mep48(e[2]).precio_OF())
                        #vender(ccl48(e[2]),comproMEP,ccl48(e[2]).precio_BI())
                        #comprar(ccl48(e[0]),comproCCL,ccl48(e[0]).precio_OF())

                        gana += comproCCL - e[1]
                        limite -= e[1]
                        print(f'{e[0]}/{e[2]} /48/ Total bonos:{gana}, total MEP: {saldoMEP}, total CCL {saldoCCL}')
                        continue
                    else:
                        print(f'NO hay /48/ {e[0]}.mep _ {e[2]}.ccl _ LIM: {limite}')
                        break
                break
            else:
                print(f'Limite actual:{limite} Sin precios 48 {e[0]}.mep _ {e[2]}.ccl')
                break
