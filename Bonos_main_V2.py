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
def pesCI(bono): 
    for tipo, valor in ticker['bonos']['CI']['peso'].items():
        if tipo == bono:
            return valor
def mep48(bono): 
    for tipo, valor in ticker['bonos']['48']['mep'].items():
        if tipo == bono:
            return valor
def mepCI(bono): 
    for tipo, valor in ticker['bonos']['CI']['mep'].items():
        if tipo == bono:
            return valor
def ccl48(bono): 
    for tipo, valor in ticker['bonos']['48']['ccl'].items():
        if tipo == bono:
            return valor
def cclCI(bono): 
    for tipo, valor in ticker['bonos']['CI']['ccl'].items():
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
    print(f'bon:{comproMEP}',end="____")   
def mep_ccl(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoMEP,comproMEP
    vendoMEP = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproMEP = round(vendoMEP / (t2/100),0)
    vendoCCL = round(comproMEP * ((t3/100)* (1-costos)),2)
    comproCCL = round(vendoCCL // (t4/100),0)
    print(time.strftime("%H:%M:%S"), f'MEP:{vendoMEP}',end="  ")
    print(f'bon:{comproMEP}',end="  ")
    print(f'CCL:{vendoCCL}',end="  ")
    print(f'bon:{comproCCL}',end="____") 
def ccl_pes(t1,t2,t3,t4):
    global vendoCCL,comproCCL,vendoPES,comproPES
    vendoCCL = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproCCL = round(vendoCCL / (t2/100),0)
    vendoPES = round(comproCCL * ((t3/100)* (1-costos)),2)
    comproPES = round(vendoPES // (t4/100),0)
    print(time.strftime("%H:%M:%S"), f'CCL:{vendoCCL}',end="  ")
    print(f'bon:{comproCCL}',end="  ")
    print(f'PES:{vendoPES}',end="  ")
    print(f'bon:{comproPES}',end="____")
def mep_pes(t1,t2,t3,t4):
    global vendoPES,comproPES,vendoMEP,comproMEP
    vendoMEP = round(((t1/100) * (1 - costos)) * ins['1'][1],2)
    comproMEP = round(vendoMEP / (t2/100),0)
    vendoPES = round(comproMEP * ((t3/100)* (1-costos)),2)
    comproPES = round(vendoPES // (t4/100),0)
    print(time.strftime("%H:%M:%S"), f'MEP:{vendoMEP}',end="  ")
    print(f'bon:{comproMEP}',end="  ")
    print(f'PES:{vendoPES}',end="  ")
    print(f'bon:{comproPES}',end="____") 

costos = 0.0052
limite = 1000
gana = 0

ins = {
    '1':['al30',100,'gd30'],'2':['0',100,'gd35'],'3':['0',100,'al35'],
    '4':['gd30',100,'al30'],'5':['0',100,'gd35'],'6':['0',100,'al35'] }

while limite >0:
    if time.strftime("%H:%M:%S") >= '17:00:10':
        print('...................... MERCADO CERRADO 17HS .......................')
        break
    for i, e in ins.items():
        while e[0] != '0':

            ccl_mep( ccl48(e[0]).precio_BI(),ccl48(e[2]).precio_OF(),mep48(e[2]).precio_BI(),mep48(e[0]).precio_OF())

            if limite > 0:
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
                            print(f'Sin compradores/vendedores {e[0]}.ccl / {e[2]}.mep')
                    else:
                        print(f'Sin precios 48hs // {e[0]}.ccl - {e[2]}.mep')
                else:
                    print(f'NO en 48hs // {e[0]}.ccl - {e[2]}.mep')
            else:
                print(f'Limite de {limite} agotado !')
                break
    
            if time.strftime("%H:%M:%S") <= '15:59:15':
                ccl_mep(cclCI(e[0]).precio_BI(),cclCI(e[2]).precio_OF(),mepCI(e[2]).precio_BI(),mepCI(e[0]).precio_OF()) 
                if limite > 0:
                    if comproMEP > e[1]:
                        if cclCI(e[0]).precio_BI() != 1000 and cclCI(e[2]).precio_OF() != 1000 and mepCI(e[0]).precio_BI() != 1000 and mepCI(e[2]).precio_OF() != 1000:

                            if cclCI(e[0]).cantidad_BI() > e[1] and cclCI(e[2]).cantidad_OF() >= comproCCL and mepCI(e[2]).cantidad_BI() >= comproCCL and mepCI(e[0]).cantidad_OF() >= comproMEP:

                                #vender(cclCI(e[0]),e[1],cclCI(e[0]).precio_BI())
                                #comprar(cclCI(e[2]),comproCCL,cclCI(e[2]).precio_OF())
                                #vender(mepCI(e[2]),comproCCL,mepCI(e[2]).precio_BI())
                                #comprar(mepCI(e[0]),comproMEP,mepCI(e[0]).precio_OF())

                                gana += comproMEP - e[1]
                                limite -= e[1]
                                print(f'Limite:{limite}, Gana:{comproMEP - e[1]}, Total:{gana}')
                            else:
                                print(f'Sin compradores/vendedores {e[0]}.ccl / {e[2]}.mep')
                        else:
                            print(f'Sin precios {e[0]}.ccl / {e[2]}.mep')
                    else:
                        print(f'NO en CI // {e[0]}.ccl - {e[2]}.mep')
                else:
                    print(f'Limite de {limite} agotado !')
                    break
            else:
                print(f'CI cerrado {e[0]}.ccl / {e[2]}.mep ... continua largo')

            mep_ccl(mep48(e[0]).precio_BI(),mep48(e[2]).precio_OF(),ccl48(e[2]).precio_BI(),ccl48(e[0]).precio_OF())

            if limite > 0:
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
                            print(f'Sin compradores/vendedores {e[0]}.mep / {e[2]}.ccl')
                    else:
                        print(f'Sin precios {e[0]}.mep / {e[2]}.ccl')
                else:
                    print(f'NO 48hs // {e[0]}.mep - {e[2]}.ccl')
            else:
                print(f'Limite de {limite} agotado !')
                break

            if time.strftime("%H:%M:%S") <= '15:59:15':
                mep_ccl(mepCI(e[0]).precio_BI(),mepCI(e[2]).precio_OF(),cclCI(e[2]).precio_BI(),cclCI(e[0]).precio_OF())
                if limite > 0:
                    if comproCCL > e[1]:
                        if mepCI(e[0]).precio_BI() != 1000 and mepCI(e[2]).precio_OF() != 1000 and cclCI(e[0]).precio_BI() != 1000 and cclCI(e[2]).precio_OF() != 1000:
                            if mepCI(e[0]).cantidad_BI() > e[1] and mepCI(e[2]).cantidad_OF() >= comproMEP and cclCI(e[2]).cantidad_BI() >= comproMEP and cclCI(e[0]).cantidad_OF() >= comproCCL:

                                #vender(mepCI(e[0]),e[1],mepCI(e[0]).precio_BI())
                                #comprar(mepCI(e[2]),comproMEP,mepCI(e[2]).precio_OF())
                                #vender(cclCI(e[2]),comproMEP,cclCI(e[2]).precio_BI())
                                #comprar(cclCI(e[0]),comproCCL,cclCI(e[0]).precio_OF())

                                gana += comproCCL - e[1]
                                limite -= e[1]
                                print(f'Limite:{limite}, Gana:{comproCCL - e[1]}, Total:{gana}')
                            else:
                                print(f'Sin compradores/vendedores {e[0]}.mep / {e[2]}.ccl')
                        else:
                            print(f'Sin precios 48hs // {e[0]}.mep - {e[2]}.ccl')
                    else:
                        print(f'NO en CI // {e[0]}.mep - {e[2]}.ccl')
                else:
                    print(f'Limite de {limite} agotado !')
                    break
            else:
                print(f'CI cerrado {e[0]}.mep / {e[2]}.ccl ... continua largo')





            '''ccl_pes(ccl48(e[0]).precio_BI(),ccl48(e[2]).precio_OF(),pes48(e[2]).precio_BI(),pes48(e[0]).precio_OF())

            if limite > 0:
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
                            print(f'Sin compradores/vendedores {e[0]}.ccl / {e[2]}.pesos')
                    else:
                        print(f'Sin precios 48hs // {e[0]}.ccl - {e[2]}.pesos')
                else:
                    print(f'NO en 48hs // {e[0]}.ccl - {e[2]}.pesos')
            else:
                print(f'Limite de {limite} agotado !')
                break


            mep_pes(mep48(e[0]).precio_BI(),mep48(e[2]).precio_OF(),pes48(e[2]).precio_BI(),pes48(e[0]).precio_OF())

            if limite > 0:
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
                            
                        else:
                            print(f'Sin compradores/vendedores {e[0]}.ccl / {e[2]}.pesos')
                    else:
                        print(f'Sin precios 48hs // {e[0]}.ccl - {e[2]}.pesos')
                else:
                    print(f'NO en 48hs // {e[0]}.ccl - {e[2]}.pesos')
            else:
                print(f'Limite de {limite} agotado !')
                break'''
                    
