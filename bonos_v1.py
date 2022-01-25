
from Consultar import Consultar
from Operar import Operar
import math
import time

pr = Consultar()
op = Operar()

costos = 0.0026
limite = 100000
gAL30 = 0
gGD30 = 0
gAAPL = 0
gS31E2 = 0
gKO = 0
pesos = round(0,2)
mep = round(0,2)
ccl = round(0,2)

moneda = {'mep-ccl':['D','D','C','C'] , 'ccl-mep':['C','C','D','D'] , 'mep-pes':['D','D','',''] , 'ccl-pes':['C','C','','']}

plazo = ['CI','48hs','24hs']

par = { '1':['al30',200,'gd30'], '2':['al30',200,'s31e2'], '3':['al30',200,'aapl'],
        '10':['gd30',200,'al30'],'11':['gd30',200,'s31e2'],'12':['gd30',200,'aapl'],
        '20':['s31e2',8000,'al30'],'21':['s31e2',8000,'gd30'],'22':['s31e2',8000,'aapl'],
        '30':['aapl',5,'al30'],'31':['aapl',5,'gd30'],'30':['aapl',5,'s31e2']
}

def ganaBonos(bono:str):
    global gAL30,gGD30,gAAPL,gS31E2
    if      bono == 'al30':     gAL30  += round(comproA - e[1],0)
    elif    bono == 'gd30':     gGD30  += round(comproA - e[1],0)
    elif    bono == 'aapl':     gAAPL  += round(comproA - e[1],0)
    elif    bono == 's31e2':    gS31E2 += round(comproA - e[1],0)
def ganaMoneda(moneda:str):
    global pesos,mep,ccl
    if moneda == 'ccl-mep':
        ccl   += round((vendoA - (comproB * (pr.precioOF('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +'') / 100) ))   ,2)
        mep   += round((vendoB - (comproA * (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +'') / 100) ))   ,2)
    elif moneda == 'mep-ccl':
        mep   += round((vendoA - (comproB * (pr.precioOF('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +'') / 100) ))   ,2)
        ccl   += round((vendoB - (comproA * (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +'') / 100) ))   ,2)
    elif moneda == 'ccl-pes':
        ccl   += round((vendoA - (comproB * (pr.precioOF('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +'') / 100) ))   ,2)
        pesos += round((vendoB - (comproA * (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +'') / 100) ))   ,2)
    elif moneda == 'mep-pes':
        mep   += round((vendoA - (comproB * (pr.precioOF('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +'') / 100) ))   ,2)
        pesos += round((vendoB - (comproA * (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +'') / 100) ))   ,2)

if time.strftime("%H:%M:%S") > '23:59:45':
    plazo = ['48hs','24hs']

def primero(ticker:str,tipo:str,plazo:str):
    global vendoA
    if ticker == 'aapl' or ticker == 'ko': 
        vendoA = pr.precioBI('MERV - XMEV - ' + tipo + plazo + ' - ' + o +'') * (1 - costos) * e[1]
        return vendoA
    else: 
        vendoA = pr.precioBI('MERV - XMEV - ' + tipo + plazo + '- ' + o +'') / 100 * (1 - costos) * e[1]
        return vendoA
def segundo(ticker:str,tipo:str,plazo:str):
    global comproB
    if ticker == 'aapl' or ticker == 'ko': 
        comproB = vendoA / pr.precioOF('MERV - XMEV - ' + ticker + tipo + ' - ' + o +'') * (1 + costos) * e[1]
        return comproB
    else: 
        comproB = vendoA / pr.precioOF('MERV - XMEV - ' + ticker + tipo + ' - ' + o +'') / 100 * (1 + costos) * e[1]
        return comproB
def tercero(ticker:str,tipo:str,plazo:str):
    global vendoB
    if ticker == 'aapl' or ticker == 'ko': 
        vendoB = comproB * pr.precioBI('MERV - XMEV - ' + ticker + tipo + ' - ' + o +'') * (1 - costos) * e[1]
        return vendoB
    else: 
        vendoB = comproB * pr.precioBI('MERV - XMEV - ' + ticker + tipo + ' - ' + o +'') / 100 * (1 - costos) * e[1]
        return vendoB
def cuarto(ticker:str,tipo:str,plazo:str):
    global comproA
    if ticker == 'aapl' or ticker == 'ko': 
        comproA = vendoB / pr.precioOF('MERV - XMEV - ' + ticker + tipo + ' - ' + o +'') * (1 - costos) * e[1]
        return comproA
    else: 
        comproA = vendoB / pr.precioOF('MERV - XMEV - ' + ticker + tipo + ' - ' + o +'') / 100 * (1 - costos) * e[1]
        return comproA

while True:
    if limite < 200 or time.strftime("%H:%M:%S") > '23:59:50':
        print(f'FIN 17HS | limite {limite} | al30 {gAL30} | gd30 {gGD30} | s31e2 {gS31E2} | aapl {gAAPL} || ccl {ccl} | mep {mep} | pesos {pesos}')
        break
    for a,e in par.items():
        for o in plazo:
            for i,u in moneda.items():

                if primero(e[0].upper(),u[0],o) == 1000: continue
                elif segundo(e[2].upper(),u[1],o) == 1000: continue
                elif tercero(e[2].upper(),u[2],o) == 1000: continue
                elif cuarto(e[0].upper(),u[3],o) == 1000: continue

                if comproA > e[1]:
                    
                    #op.vender   ( ('MERV - XMEV - ' + e[0].upper() + u[0] + ' - ' + o +''), e[1],       pr.precioBI('MERV - XMEV - ' + e[0].upper() + u[0] + ' - ' + o +'') )
                    #op.comprar  ( ('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +''), comproB,    pr.precioOF('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +'') )
                    #op.vender   ( ('MERV - XMEV - ' + e[2].upper() + u[2] + ' - ' + o +''), comproB,    pr.precioBI('MERV - XMEV - ' + e[2].upper() + u[2] + ' - ' + o +'') )
                    #op.comprar  ( ('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +''), comproA,    pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +'') )

                    print(f'SI  | limite {limite} | al30 {gAL30} | gd30 {gGD30} | s31e2 {gS31E2} | aapl {gAAPL} | ccl {ccl} | mep {mep} | pesos {pesos}')

                    pr.log('AL30: ' + str(gAL30) + ' | GD30: ' + str(gGD30) + ' | S31E2: ' + str(gS31E2) + ' | AAPL: ' + str(gAAPL) + ' || MEP: ' + str(mep) + ' | CCL: ' + str(ccl) + ' | PESOS: ' + str(pesos)    )

                    ganaBonos(e[0])
                    ganaMoneda(i)

                    if e[0] == 'al30' or e[2] == 'al30':
                        limite -= comproA - e[1]
                    continue
                else: print(time.strftime("%H:%M:%S"),f' NO | {i} | {e[0].upper()} / {e[2].upper()} {o} | limite {limite} | al30 {gAL30} | gd30 {gGD30} | s31e2 {gS31E2} | aapl {gAAPL} || ccl {ccl} | mep {mep} | pesos {pesos}')
