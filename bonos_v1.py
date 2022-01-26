
from Consultar import Consultar
from Operar import Operar
import math
import time

pr = Consultar()
op = Operar()

costos = 0.0026
limite = 300
gAL30 = 0
gGD30 = 0
gAAPL = 0
gS31E2 = 0
gKO = 0

pesos = round(0,2)
mep = round(0,2)
ccl = round(0,2)

moneda = {'ccl-mep':['C','D'],  'mep-ccl':['D','C'],  'mep-pes':['D',''] , 'ccl-pes':['C','']}

plazo = ['CI','48hs','24hs']

par = { '1':['al30',10,'gd30'], '2':['al30',10,'s31e2'],# '3':['al30',200,'aapl'],
        '10':['gd30',10,'al30'], '11':['gd30',10,'s31e2'],# '12':['gd30',200,'aapl'],
        '20':['s31e2',8000,'al30'], '21':['s31e2',8000,'gd30'],# '22':['s31e2',8000,'aapl'],
        '30':['aapl',5,'al30'], '31':['aapl',5,'gd30'], '30':['aapl',5,'s31e2']           
        }

def ganaBonos(bono:str):
    global gAL30,gGD30,gAAPL,gS31E2
    if      bono == 'al30':     gAL30  += int(comproA - e[1])
    elif    bono == 'gd30':     gGD30  += int(comproA - e[1])
    elif    bono == 'aapl':     gAAPL  += int(comproA - e[1])
    elif    bono == 's31e2':    gS31E2 += int(comproA - e[1])

def ganaMoneda(moneda:str):
    global pesos,mep,ccl
    if moneda == 'ccl-mep':
        if e[0] == 'aapl' or e[0] == 'ko': 
            ccl     += round( vendoA - (comproB *  precioB ), 3)
            mep     += round( vendoB - (comproA *  precioA ), 3)
        else:                              
            ccl     += round( vendoA - (comproB * (precioB / 100) ), 3)
            mep     += round( vendoB - (comproA * (precioA / 100) ), 3)

    elif moneda == 'mep-ccl':
        if e[0] == 'aapl' or e[0] == 'ko':
            mep     += round( vendoA - (comproB *  precioB ), 3)
            ccl     += round( vendoB - (comproA *  precioA ), 3)
        else:                              
            mep     += round( vendoA - (comproB * (precioB / 100) ), 3)
            ccl     += round( vendoB - (comproA * (precioA / 100) ), 3)

    elif moneda == 'ccl-pes':
        if e[0] == 'aapl' or e[0] == 'ko':
            ccl     += round( vendoA - (comproB *  precioB ), 3)
            pesos   += round( vendoB - (comproA *  precioA ), 3)
        else:                              
            ccl     += round( vendoA - (comproB * (precioB / 100) ), 3)
            pesos   += round( vendoB - (comproA * (precioA / 100) ), 3)

    elif moneda == 'mep-pes':
        if e[0] == 'aapl' or e[0] == 'ko':
            mep     += round( vendoA - (comproB *  precioB ), 3)
            pesos   += round( vendoB - (comproA *  precioA ), 3)
        else:                              
            mep     += round( vendoA - (comproB * (precioB / 100) ), 3)
            pesos   += round( vendoB - (comproA * (precioA / 100) ), 3)

def cruzar(veA,coB,veB,coA):
    global comproA, comproB, vendoB, vendoA,    precioA, precioB, precioC, precioD

    precioA = pr.precioBI('MERV - XMEV - ' + veA + u[0] + ' - ' + o +'')
    if e[0] == 'aapl' or e[0] == 'ko': 
        vendoA = round( precioA * e[1]  * ( 1 - costos), 2)
    else:                                 
        vendoA = round((precioA / 100) * e[1]  * ( 1 - costos), 2)

    precioB = pr.precioOF('MERV - XMEV - ' + coB + u[1] + ' - ' + o +'')
    if e[2] == 'aapl' or e[2] == 'ko': 
        comproB = vendoA // round( precioB * ( 1 + costos),2)
    else:                                 
        comproB = vendoA // round((precioB/100) * ( 1 + costos),2)

    precioC = pr.precioBI('MERV - XMEV - ' + veB + u[1] + ' - ' + o +'')
    if e[2] == 'aapl' or e[2] == 'ko': 
        vendoB = comproB * round( precioC * ( 1 - costos),2)
    else:                                 
        vendoB = comproB * round((precioC/100) * ( 1 - costos),2)

    precioD = pr.precioOF('MERV - XMEV - ' + coA + u[0] + ' - ' + o +'')
    if e[0] == 'aapl' or e[0] == 'ko': 
        comproA = vendoB // round( precioD * ( 1 + costos),2)
        if precioA != 1000 and precioB != 1000 and precioC != 1000 and precioD != 1000: return comproA
        else: 
            comproA = 1000
            return comproA
    else: 
        comproA = vendoB // round((precioD / 100) * ( 1 + costos),2)
        if precioA != 1000 and precioB != 1000 and precioC != 1000 and precioD != 1000: return comproA
        else:  
            comproA = 1000
            return comproA

if time.strftime("%H:%M:%S") > '15:59:45': plazo = ['48hs','24hs']

################################

while True:
    if time.strftime("%H:%M:%S") < '11:00:00':
        print(time.strftime("%H:%M:%S"),'Esperando la apertura a las 11hs ... '),time.sleep(10)
        continue
    if time.strftime("%H:%M:%S") > '23:59:50':
        print(f'FIN 17HS CERRADO !!!   | limite {limite} | al30 {gAL30} | gd30 {gGD30} | s31e2 {gS31E2} | aapl {gAAPL} || ccl {ccl} | mep {mep} | pesos {pesos}')
        break
    if limite < 200: 
        print(f'FIN LIMITE AGOTADO !!! | limite {limite} | al30 {gAL30} | gd30 {gGD30} | s31e2 {gS31E2} | aapl {gAAPL} || ccl {ccl} | mep {mep} | pesos {pesos}')
        break  
    
    for a,e in par.items():
        for o in plazo:
            for i,u in moneda.items(): 

                cruzar(     e[0].upper(),   e[2].upper(),   e[2].upper(),   e[0].upper()    )

                if comproA == 1000: 
                    print(f'Sin precios {e[0].upper()}{u[0]} {o} conta {e[2].upper()}{u[0]} {o} '),time.sleep(1)
                    break

                if limite < 200:  break

                if comproA > e[1]:

                    if e[0] == 'al30' or e[2] == 'al30': limite -= int( e[1] )

                    #op.vender   ( ('MERV - XMEV - ' + e[0].upper() + u[0] + ' - ' + o +''), e[1],       pr.precioBI('MERV - XMEV - ' + e[0].upper() + u[0] + ' - ' + o +'') )
                    #op.comprar  ( ('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +''), comproB,    pr.precioOF('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +'') )
                    #op.vender   ( ('MERV - XMEV - ' + e[2].upper() + u[2] + ' - ' + o +''), comproB,    pr.precioBI('MERV - XMEV - ' + e[2].upper() + u[2] + ' - ' + o +'') )
                    #op.comprar  ( ('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +''), comproA,    pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +'') )

                    ganaBonos(e[0])
                    ganaMoneda(i)

                    print(f'    SI | limite {limite} | al30 {gAL30} | gd30 {gGD30} | s31e2 {gS31E2} | aapl {gAAPL} | ccl {ccl} | mep {mep} | pesos {pesos}')
                        
                    pr.log('AL30: ' + str(gAL30) + ' | GD30: ' + str(gGD30) + ' | S31E2: ' + str(gS31E2) + ' | AAPL: ' + str(gAAPL) + ' || MEP: ' + str(mep) + ' | CCL: ' + str(ccl) + ' | PESOS: ' + str(pesos))
                        
                else: 
                    print(time.strftime("%H:%M:%S"),f' NO | {i} | {e[0].upper()} / {e[2].upper()} {o} | limite {limite} | al30 {gAL30} | gd30 {gGD30} | s31e2 {gS31E2} | aapl {gAAPL} || ccl {ccl} | mep {mep} |pesos {pesos}')
                    break
                           