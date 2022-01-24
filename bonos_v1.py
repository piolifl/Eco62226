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
pesos = 0
mep = 0
ccl = 0

moneda = {'ccl-mep':['C','C','D','D'] ,'mep-ccl':['D','D','C','C'],'ccl-pes':['C','C','',''],'mep-pes':['D','D','','']}

plazo = ['CI','48hs','24hs']

par = { '1':['al30',200,'gd30'],'2':['al30',200,'s31e2'],'3':['al30',200,'aapl'],
        '10':['gd30',200,'al30'],'11':['gd30',200,'s31e2'],'12':['gd30',200,'aapl'],
        '20':['s31e2',8000,'al30'],'21':['s31e2',8000,'gd30'],'22':['s31e2',8000,'aapl'],
        '30':['aapl',5,'al30'],'31':['aapl',5,'gd30'],'30':['aapl',5,'s31e2']
}

def ganaBonos(bono):
    global gAL30,gGD30,gAAPL,gS31E2
    if      bono == 'al30':     gAL30  += comproA - e[1]
    elif    bono == 'gd30':     gGD30  += comproA - e[1]
    elif    bono == 'aapl':     gAAPL  += comproA - e[1]
    elif    bono == 's31e2':    gS31E2 += comproA - e[1]
def ganaMoneda(moneda):
    global pesos,mep,ccl
    if moneda == 'ccl-mep':
        ccl   += (vendoA - (comproB / (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +''))   *   (1 + costos) ))
        mep   += (vendoB - (comproA / (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +''))   *   (1 + costos) ))
    elif moneda == 'mep-ccl':
        mep   += (vendoA - (comproB / (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +''))   *   (1 + costos) ))
        ccl   += (vendoB - (comproA / (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +''))   *   (1 + costos) ))
    elif moneda == 'ccl-pes':
        ccl     += (vendoA - (comproB / (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +''))   *   (1 + costos) ))
        pesos   += (vendoB - (comproA / (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +''))   *   (1 + costos) ))
    elif moneda == 'mep-pes':
        mep     += (vendoA - (comproB / (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +''))   *   (1 + costos) ))
        pesos   += (vendoB - (comproA / (pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +''))   *   (1 + costos) ))

if time.strftime("%H:%M:%S") > '15:59:45':
    plazo = ['48hs','24hs']

while True:
    if limite < 200 or time.strftime("%H:%M:%S") > '16:59:50':
        print(f'FIN 17HS | limite {limite} | al30 {gAL30} | gd30 {gGD30} | s31e2 {gS31E2} | aapl {gAAPL} | ccl {ccl} | mep {mep} | pesos {pesos}')
        break
    for a,e in par.items():
        for o in plazo:
            for i,u in moneda.items():

                if e[0] == 'aapl' or e[0] == 'ko': 
                    precio = pr.precioBI('MERV - XMEV - ' + e[0].upper() + u[0] + ' - ' + o +'')
                    if precio == 1000: break
                    else: vendoA = round( (  precio  *   (1 - costos))  *  e[1], 2)
                else: 
                    precio = pr.precioBI('MERV - XMEV - ' + e[0].upper() + u[0] + ' - ' + o +'')
                    if precio == 1000: break
                    else: vendoA = round( (  ( precio / 100)  *   (1 - costos))  *  e[1], 2)

                if e[2] == 'aapl' or e[2] == 'ko':
                    precio = pr.precioOF('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +'')
                    if precio == 1000: break
                    else: comproB = round( vendoA   /  precio   *   (1 + costos), 0)
                else: 
                    precio = pr.precioOF('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +'')
                    if precio == 1000: break
                    else: comproB = round( vendoA   /  (precio  / 100)   *   (1 + costos), 0)

                if e[2] == 'aapl' or e[2] == 'ko':
                    precio = pr.precioBI('MERV - XMEV - ' + e[2].upper() + u[2] + ' - ' + o +'')
                    if precio == 1000: break
                    else: vendoB = round( comproB  *  precio   *   (1 - costos), 2)
                else: 
                    precio = pr.precioBI('MERV - XMEV - ' + e[2].upper() + u[2] + ' - ' + o +'')
                    if precio == 1000: break
                    else: vendoB = round( comproB  *  (precio  / 100)   *   (1 - costos), 2)

                if e[0] == 'aapl' or e[0] == 'ko':
                    precio = pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +'')
                    if precio == 1000: break
                    comproA = round( vendoB   /  precio   *   (1 + costos), 0)
                else: 
                    precio = pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +'')
                    if precio == 1000: break
                    comproA = round( vendoB   /  (precio  / 100)   *   (1 + costos), 0)

                if comproA > e[1]:
                    
                    #op.vender   ( ('MERV - XMEV - ' + e[0].upper() + u[0] + ' - ' + o +''), e[1],       pr.precioBI('MERV - XMEV - ' + e[0].upper() + u[0] + ' - ' + o +'') )
                    #op.comprar  ( ('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +''), comproB,    pr.precioOF('MERV - XMEV - ' + e[2].upper() + u[1] + ' - ' + o +'') )
                    #op.vender   ( ('MERV - XMEV - ' + e[2].upper() + u[2] + ' - ' + o +''), comproB,    pr.precioBI('MERV - XMEV - ' + e[2].upper() + u[2] + ' - ' + o +'') )
                    #op.comprar  ( ('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +''), comproA,    pr.precioOF('MERV - XMEV - ' + e[0].upper() + u[3] + ' - ' + o +'') )

                    print(f'SI GANA | limite {limite} | al30 {gAL30} | gd30 {gGD30} | s31e2 {gS31E2} | aapl {gAAPL} | ccl {ccl} | mep {mep} | pesos {pesos}')

                    ganaBonos(e[0])
                    ganaMoneda(i)

                    if e[0] == 'al30' or e[2] == 'al30': 
                        limite -= comproA - e[1]
                        continue
                else: print(time.strftime("%H:%M:%S"),f' NO | {i} | {e[0].upper()} / {e[2].upper()} {o} | limite {limite} | al30 {gAL30} | gd30 {gGD30} | s31e2 {gS31E2} | aapl {gAAPL} | ccl {ccl} | mep {mep} | pesos {pesos}')
