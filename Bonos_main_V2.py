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
    comproCCL = round(vendoCCL / ((t2/100 )* (1 + costos)),0)
    vendoMEP = round(comproCCL * ((t3/100) * (1-costos)),2)
    comproMEP = round(vendoMEP / ((t4/100) * (1 + costos)),0)

    saldoCCL = round(vendoCCL - comproCCL * (t2/100),2)
    saldoMEP = round(vendoMEP - comproMEP * (t4/100),2)
    print(time.strftime("%H:%M:%S"),f' _ CCL:{vendoCCL}',end="  ")
    print(f'bon:{comproCCL}',end="  ")
    print(f'MEP:{vendoMEP}',end="  ")
    print(f'bon:{comproMEP}',end=" _ ")
def mep_ccl(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoMEP,comproMEP,saldoMEP,saldoCCL
    vendoMEP = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproMEP = round(vendoMEP / ((t2/100) * (1 + costos)),0)
    vendoCCL = round(comproMEP * ((t3/100) * (1-costos)),2)
    comproCCL = round(vendoCCL / ((t4/100) * (1 + costos)),0)
    saldoMEP = round(vendoMEP - comproMEP * (t2/100),2)
    saldoCCL = round(vendoCCL - comproCCL * (t4/100),2)
    print(time.strftime("%H:%M:%S"),f' _ MEP:{vendoMEP}',end="  ")
    print(f'bon:{comproMEP}',end="  ")
    print(f'CCL:{vendoCCL}',end="  ")
    print(f'bon:{comproCCL}',end=" _ ")
def ccl_pes(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoPES,comproPES,saldoCCL, saldoPES
    vendoCCL = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproCCL = round(vendoCCL / ((t2/100) * (1 + costos)),0)
    vendoPES = round(comproCCL * ((t3/100) * (1-costos)),2)
    comproPES = round(vendoPES / ((t4/100) * (1 + costos)),0)
    saldoCCL = round(vendoCCL - comproCCL * (t2/100),2)
    saldoPES = round(vendoPES - comproPES * (t4/100),2)
    print(time.strftime("%H:%M:%S"),f' _ CCL:{vendoCCL}',end="  ")
    print(f'bon:{comproCCL}',end="  ")
    print(f'PES:{vendoPES}',end="  ")
    print(f'bon:{comproPES}',end=" _ ")
def mep_pes(t1,t2,t3,t4):
    global vendoPES,comproPES,vendoMEP,comproMEP,saldoMEP,saldoPES
    vendoMEP = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproMEP = round(vendoMEP / ((t2/100) * (1 + costos)),0)
    vendoPES = round(comproMEP * ((t3/100) * (1-costos)),2)
    comproPES = round(vendoPES / ((t4/100) * (1 + costos)),0)
    saldoMEP = round(vendoMEP - comproMEP * (t2/100),2)
    saldoPES = round(vendoPES - comproPES * (t4/100),2)
    print(time.strftime("%H:%M:%S"),f' _ MEP:{vendoMEP}',end="  ")
    print(f'bon:{comproMEP}',end="  ")
    print(f'PES:{vendoPES}',end="  ")
    print(f'bon:{comproPES}',end=" _ ") 

costos = 0.0026
limite = 1000
gana = round(0,0)
ccl = round(0,4)
mep = round(0,4)
peso = round(0,4)

ins = {
    '1':['al30',100,'gd30'],'2':['0',100,'s31e2'],
    '3':['0',100,'al30'],'4':['0',100,'s31e2'],
    '5':['0',5000,'al30'],'6':['0',5000,'gd30']}


while limite > 0:
    if time.strftime("%H:%M:%S") >= '17:00:10':
        print('...................... MERCADO CERRADO 17HS .......................')
        break
    for i, e in ins.items():
        while e[0] != '0':
            if time.strftime("%H:%M:%S") <= '15:59:15':

                t1 = cclCI(e[0]).precio_BI()
                t2 = cclCI(e[2]).precio_OF()
                t3 = mepCI(e[2]).precio_BI()
                t4 = mepCI(e[0]).precio_OF()
                if t1 != 1000 and t2 != 1000 and t3 != 1000 and t4 != 1000:
                    while limite > 0:
                        ccl_mep(t1,t2,t3,t4)
                        if comproMEP >= e[1] and cclCI(e[0]).cantidad_BI() > e[1] and cclCI(e[2]).cantidad_OF() >= comproCCL and mepCI(e[2]).cantidad_BI() >= comproCCL and mepCI(e[0]).cantidad_OF() >= comproMEP:

                            #vender(cclCI(e[0]),e[1],cclCI(e[0]).precio_BI())
                            #comprar(cclCI(e[2]),comproCCL,cclCI(e[2]).precio_OF())
                            #vender(mepCI(e[2]),comproCCL,mepCI(e[2]).precio_BI())
                            #comprar(mepCI(e[0]),comproMEP,mepCI(e[0]).precio_OF())

                            gana += comproMEP - e[1]
                            limite -= e[1]
                            ccl += saldoCCL
                            mep += saldoMEP
                            print(f'CI {e[0]}/{e[2]}, ganados:{gana}, {ccl} CCL y {mep} MEP _ limite: {limite}')
                            continue
                        else:
                            print(f'NO hay /CI/ {e[0]}.ccl _ {e[2]}.mep _ LIM: {limite}')
                            break
                else:
                    print(f'Sin precios CI para {e[0]}.ccl _ {e[2]}.mep')
                    break

                t1 = mepCI(e[0]).precio_BI()
                t2 = mepCI(e[2]).precio_OF()
                t3 = cclCI(e[2]).precio_BI()
                t4 = cclCI(e[0]).precio_OF()
                if t1 != 1000 and t2 != 1000 and t3 != 1000 and t4 != 1000:
                    while limite > 0:
                        mep_ccl(t1,t2,t3,t4)
                        if comproCCL >= e[1] and mepCI(e[0]).cantidad_BI() > e[1] and mepCI(e[2]).cantidad_OF() > comproMEP and cclCI(e[2]).cantidad_BI() >= comproMEP and cclCI(e[0]).cantidad_OF() >= comproCCL:

                            #vender(mepCI(e[0]),e[1],mepCI(e[0]).precio_BI())
                            #comprar(mepCI(e[2]),comproMEP,mepCI(e[2]).precio_OF())
                            #vender(cclCI(e[2]),comproMEP,cclCI(e[2]).precio_BI())
                            #comprar(cclCI(e[0]),comproCCL,cclCI(e[0]).precio_OF())

                            gana += comproCCL - e[1]
                            limite -= e[1]
                            ccl += saldoCCL
                            mep += saldoMEP
                            print(f'CI {e[0]}/{e[2]}, ganados:{gana} bonos, {mep} MEP y {ccl} CCL _ limite: {limite}')
                            continue
                        else:
                            print(f'NO hay /CI/ {e[0]}.mep _ {e[2]}.ccl _ LIM: {limite}')
                            break
                else:
                    print(f'Sin precios CI para {e[0]}.mep _ {e[2]}.ccl')
                    break

                t1 = cclCI(e[0]).precio_BI()
                t2 = cclCI(e[2]).precio_OF()
                t3 = pesCI(e[2]).precio_BI()
                t4 = pesCI(e[0]).precio_OF()
                if t1 != 1000 and t2 != 1000 and t3 != 1000 and t4 != 1000:
                    while limite > 0:
                        ccl_pes(t1,t2,t3,t4)
                        if comproPES >= e[1] and cclCI(e[0]).cantidad_BI() > e[1] and cclCI(e[2]).cantidad_OF() > comproCCL and pesCI(e[2]).cantidad_BI() >= comproCCL and pesCI(e[0]).cantidad_OF() >= comproPES:

                            #vender(cclCI(e[0]),e[1],cclCI(e[0]).precio_BI())
                            #comprar(cclCI(e[2]),comproCCL,cclCI(e[2]).precio_OF())
                            #vender(pesCI(e[2]),comproCCL,pesCI(e[2]).precio_BI())
                            #comprar(pesCI(e[0]),comproPES,pesCI(e[0]).precio_OF())

                            gana += comproPES - e[1]
                            limite -= e[1]
                            ccl += saldoCCL
                            peso += saldoPES
                            print(f'CI {e[0]}/{e[2]}, ganados:{gana}, {ccl} CCL y {peso} PES _ limite: {limite}')
                            continue
                        else:
                            print(f'NO hay /CI/ {e[0]}.ccl _ {e[2]}.peso _ LIM: {limite}')
                            break
                else:
                    print(f'Sin precios CI para {e[0]}.ccl _ {e[2]}.peso')
                    break

                t1 = mepCI(e[0]).precio_BI()
                t2 = mepCI(e[2]).precio_OF()
                t3 = pesCI(e[2]).precio_BI()
                t4 = pesCI(e[0]).precio_OF()
                if t1 != 1000 and t2 != 1000 and t3 != 1000 and t4 != 1000:
                    while limite > 0:
                        mep_pes(t1,t2,t3,t4)
                        if comproPES >= e[1] and mepCI(e[0]).cantidad_BI() > e[1] and mepCI(e[2]).cantidad_OF() > comproCCL and pesCI(e[2]).cantidad_BI() >= comproCCL and pesCI(e[0]).cantidad_OF() >= comproPES:

                            #vender(mepCI(e[0]),e[1],mepCI(e[0]).precio_BI())
                            #comprar(mepCI(e[2]),comproMEP,mepCI(e[2]).precio_OF())
                            #vender(pesCI(e[2]),comproMEP,pesCI(e[2]).precio_BI())
                            #comprar(pesCI(e[0]),comproPES,pesCI(e[0]).precio_OF())

                            gana += comproPES - e[1]
                            limite -= e[1]
                            peso += saldoPES
                            mep += saldoMEP
                            print(f'CI {e[0]}/{e[2]}, ganados:{gana} bonos, {mep} MEP y {peso} PES _ limite: {limite}')
                            continue
                        else:
                            print(f'NO hay /CI/ {e[0]}.mep _ {e[2]}.peso _ LIM: {limite}')
                            break
                else:
                    print(f'Sin precios CI para {e[0]}.mep _ {e[2]}.peso')
                    break

        # CCL contra MEP en 48 horas
            t1 = ccl48(e[0]).precio_BI()
            t2 = ccl48(e[2]).precio_OF()
            t3 = mep48(e[2]).precio_BI()
            t4 = mep48(e[0]).precio_OF()
            if t1 != 1000 and t2 != 1000 and t3 != 1000 and t4 != 1000:
                while limite > 0:
                    ccl_mep(t1,t2,t3,t4)
                    if comproMEP >= e[1] and ccl48(e[0]).cantidad_BI() > e[1] and ccl48(e[2]).cantidad_OF() >= comproCCL and mep48(e[2]).cantidad_BI() >= comproCCL and mep48(e[0]).cantidad_OF() >= comproMEP:

                        #vender(ccl48(e[0]),e[1],ccl48(e[0]).precio_BI())
                        #comprar(ccl48(e[2]),comproCCL,ccl48(e[2]).precio_OF())
                        #vender(mep48(e[2]),comproCCL,mep48(e[2]).precio_BI())
                        #comprar(mep48(e[0]),comproMEP,mep48(e[0]).precio_OF())

                        gana += comproMEP - e[1]
                        limite -= e[1]
                        ccl += saldoCCL
                        mep += saldoMEP
                        print(f'48 {e[0]}/{e[2]}, ganados:{gana}, {ccl} CCL y {mep} MEP _ limite: {limite}')
                        continue
                    else:
                        print(f'NO hay /48/ {e[0]}.ccl _ {e[2]}.mep _ LIM: {limite}')
                        break
            else:
                print(f'Sin precios 48 para {e[0]}.ccl _ {e[2]}.mep')
                break

        # MEP contra CCL en 48 horas
            t1 = mep48(e[0]).precio_BI()
            t2 = mep48(e[2]).precio_OF()
            t3 = ccl48(e[2]).precio_BI()
            t4 = ccl48(e[0]).precio_OF()
            if t1 != 1000 and t2 != 1000 and t3 != 1000 and t4 != 1000:
                while limite > 0:
                    mep_ccl(t1,t2,t3,t4)
                    if comproCCL >= e[1] and mep48(e[0]).cantidad_BI() > e[1] and mep48(e[2]).cantidad_OF() >= comproMEP and ccl48(e[2]).cantidad_BI() >= comproMEP and ccl48(e[0]).cantidad_OF() >= comproCCL:

                        #vender(mep48(e[0]),e[1],mep48(e[0]).precio_BI())
                        #comprar(mep48(e[2]),comproMEP,mep48(e[2]).precio_OF())
                        #vender(ccl48(e[2]),comproMEP,ccl48(e[2]).precio_BI())
                        #comprar(ccl48(e[0]),comproCCL,ccl48(e[0]).precio_OF())

                        gana += comproCCL - e[1]
                        limite -= e[1]
                        ccl += saldoCCL
                        mep += saldoMEP
                        print(f'48 {e[0]}/{e[2]}, ganados:{gana} bonos, {mep} MEP y {ccl} CCL _ limite: {limite}')
                        continue
                    else:
                        print(f'NO hay /48/ {e[0]}.mep _ {e[2]}.ccl _ LIM: {limite}')
                        break
                break
            else:
                print(f'Sin precios 48 para {e[0]}.mep _ {e[2]}.ccl')
                break



