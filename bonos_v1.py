from Consultar import Consultar
from Operar import Operar
import math
import time

pr = Consultar()
op = Operar()

costos = 0.0026
limite = 1000
al30 = 0
gd30 = 0
aapl = 0
ko = 0
s28f2 = 0
ccl = 0
mep = 0
peso = 0

moneda = {'ccl-mep':['C','D'],  'mep-ccl':['D','C'],  #'mep-pes':['D',''] , 'ccl-pes':['C','']
}

plazo = ['CI','48hs','24hs'
]

par = { 
    #'0':['al30',200,'gd30'],'01':['gd30',200,'al30'],
    '1':['al30',200,'gd30'],'2':['al30',200,'ae38'],'3':['al30',200,'al29'],'4':['al30',200,'al35'],'5':['al30',200,'al41'],'6':['ae38',200,'al30'],'7':['al29',200,'al30'],'8':['al35',200,'al30'],'9':['al41',200,'al30'],
    '10':['al30',200,'gd29'],'11':['al30',200,'gd35'],'12':['al30',200,'gd38'],'13':['al30',200,'gd41'],'14':['al30',200,'gd46'],'15':['gd29',200,'al30'],'16':['gd35',200,'al30'],'17':['gd38',200,'al30'],'18':['gd41',200,'al30'],'19':['gd46',200,'al30'],
    '20':['al30',200,'s28f2'],'20':['al30',200,'s31m2'],
    '30':['al30',200,'aapl'],'31':['al30',200,'ko'],

    '100':['gd30',200,'gd29'],'101':['gd30',200,'gd35'],'102':['gd30',200,'gd38'],'103':['gd30',200,'gd41'],'104':['gd30',200,'gd46'],'105':['gd29',200,'gd30'],'106':['gd35',200,'gd30'],'107':['gd38',200,'gd30'],'108':['gd41',200,'gd30'],'109':['gd46',200,'gd30'],

    '110':['gd30',200,'al30'],'111':['gd30',200,'ae38'],'112':['gd30',200,'al29'],'113':['gd30',200,'al35'],'114':['gd30',200,'al41'],'115':['ae38',200,'gd30'],'116':['al29',200,'gd30'],'117':['al35',200,'gd30'],'118':['al41',200,'gd30'],

    '120':['gd30',200,'s28f2'],'121':['gd30',200,'s31m2'],
    '130':['gd30',200,'aapl'],'131':['gd30',200,'ko'],

    '200':['s28f2',8000,'al30'], '201':['s28f2',8000,'gd30'],'202':['s28f2',8000,'aapl'],'203':['s28f2',8000,'ko'],'204':['s28f2',8000,'s31m2'],

    '300':['aapl',5,'al30'],'301':['aapl',5,'gd30'],'302':['aapl',5,'ko'],'303':['aapl',5,'s28f2'],'304':['aapl',5,'s31m2'],
    '400':['ko',5,'al30'],'401':['ko',5,'gd30'],'402':['ko',5,'aapl'],'403':['ko',5,'s28f2'],'404':['ko',5,'s31m2']

        }

def ganaBonos(tipo):
    global al30,gd30,aapl,ko,s28f2
    if   tipo == 'al30':   al30 += int(comproA - valor[1])
    elif tipo == 'gd30':   gd30 += int(comproA - valor[1])
    elif tipo == 'aapl':   aapl += int(comproA - valor[1])
    elif tipo == 'ko':       ko += int(comproA - valor[1])
    elif tipo == 's28f2': s28f2 += int(comproA - valor[1])
def ganaMoneda(tipo):
    global ccl, mep, peso
    if tipo == 'ccl-mep': 
        ccl += vendoA - round(comproB * pr_comproB,2)
        mep += vendoB - round(comproA * pr_comproA,2)
    elif tipo == 'mep-ccl': 
        mep += vendoA - round(comproB * pr_comproB,2)
        ccl += vendoB - round(comproA * pr_comproA,2)
    elif tipo == 'ccl-pes': 
        ccl  += vendoA - round(comproB * pr_comproB,2)
        peso += vendoB - round(comproA * pr_comproA,2)
    elif tipo == 'mep-pes': 
        mep  += vendoA - round(comproB * pr_comproB,2)
        peso += vendoB - round(comproA * pr_comproA,2)

while True:
    if time.strftime("%H:%M:%S") < '11:00:00':
        print(time.strftime("%H:%M:%S"),'Esperando la apertura a las 11hs ... '),time.sleep(10)
        continue
    if time.strftime("%H:%M:%S") > '16:59:50':
        print(f'FIN 17hs CERRADO | lim{limite} | al30 {al30} | gd30 {gd30} | s28f2 {s28f2} | aapl {aapl} | ko {ko} | > ccl {ccl} mep {mep} pesos {peso} ')
        break
    if limite < 199: 
        print(f'FIN LIMITE AGOTADO | lim{limite} | al30 {al30} | gd30 {gd30} | s28f2 {s28f2} | aapl {aapl} | ko {ko} | > ccl {ccl} mep {mep} pesos {peso}  ')
        break 
    if time.strftime("%H:%M:%S") > '15:59:45': plazo = ['48hs','24hs']

    for clave,valor in par.items():
        for e,i in moneda.items():
            for u in plazo:
                while True:
                    if limite < 199: break
                    pr_vendoA =   pr.precioBI( 'MERV - XMEV - ' + valor[0].upper() + i[0] + ' - ' + u )
                    pr_comproB =  pr.precioOF( 'MERV - XMEV - ' + valor[2].upper() + i[0] + ' - ' + u )
                    pr_vendoB =   pr.precioBI( 'MERV - XMEV - ' + valor[2].upper() + i[1] + ' - ' + u )
                    pr_comproA =  pr.precioOF( 'MERV - XMEV - ' + valor[0].upper() + i[1] + ' - ' + u )
                    if pr_vendoA == 1000 or pr_comproB == 1000 or pr_vendoB == 1000 or pr_comproA == 1000: break

                    if valor[0] == 'aapl' or valor[0] == 'ko': vendoA = round(pr_vendoA * (1-costos),2) * valor[1]
                    else: vendoA = round((pr_vendoA/100) * (1-costos),2) * valor[1]
                    if valor[2] == 'aapl' or valor[2] == 'ko': comproB = vendoA // round(pr_comproB * (1+costos),2)
                    else: comproB = vendoA // round((pr_comproB/100) * (1+costos),2)
                    if valor[2] == 'aapl' or valor[2] == 'ko': vendoB = round(pr_vendoB * (1-costos),2) * comproB
                    else: vendoB = comproB * round((pr_vendoB/100) * (1-costos),2)
                    if valor[0] == 'aapl' or valor[0] == 'ko': comproA = vendoB // round(pr_comproA * (1+costos),2)
                    else: comproA = vendoB // round((pr_comproA/100) * (1+costos),2)

                    if comproA > valor[1]: 

                        if   pr.bidsBI(   'MERV - XMEV - ' + valor[0].upper() + i[0] + ' - ' + u ) < valor[1]: continue
                        elif pr.offersOF( 'MERV - XMEV - ' + valor[2].upper() + i[0] + ' - ' + u ) < comproB:  continue
                        elif pr.bidsBI(   'MERV - XMEV - ' + valor[2].upper() + i[0] + ' - ' + u ) < comproB:  continue
                        elif pr.offersOF( 'MERV - XMEV - ' + valor[0].upper() + i[0] + ' - ' + u ) < comproA:  continue
                            
                        #CUENTA EN ECO_62226
                        #op.vender   ( ( 'MERV - XMEV - ' + valor[0].upper() + i[0] + ' - ' + u )   , e[1],       pr_vendoA )
                        #op.comprar  ( ( 'MERV - XMEV - ' + valor[2].upper() + i[0] + ' - ' + u )   , comproB,    pr_comproB )
                        #op.vender   ( ( 'MERV - XMEV - ' + valor[2].upper() + i[1] + ' - ' + u )   , comproB,    pr_vendoB )
                        #op.comprar  ( ( 'MERV - XMEV - ' + valor[0].upper() + i[1] + ' - ' + u )   , comproA,    pr_comproA )

                        ganaBonos(valor[0])
                        ganaMoneda(i)

                        print(time.strftime("%H:%M:%S"),f' | SI | {e} {valor[0]} {valor[2]} {u} |  limite {limite} | al30 {al30} | gd30 {gd30} | s28f2 {s28f2} | aapl {aapl} | ko {ko} | > ccl {ccl} mep {mep} pesos {peso}  ')

                        pr.logRulos(str(e) + ' AL30: ' + str(al30) + ' | GD30: ' + str(gd30) + ' | S28F2: ' + str(s28f2) + ' | AAPL: ' + str(aapl) + ' | KO: ' + str(ko) + '| > ccl ' + str(ccl) + ' mep ' + str(mep) + ' pesos ' + str(peso) )

                        if valor[0] == 'al30' or valor[2] == 'al30': limite -= valor[1]    
                        continue                         
                    else: 
                        print(time.strftime("%H:%M:%S"),f'| NO | {comproA} | {e} {valor[0]} {valor[2]} {u} | limite {limite} |al30 {al30}|gd30 {gd30}|s28f2 {s28f2}|aapl {aapl}|ko {ko}| > ccl {ccl} mep {mep} pesos {peso}')
                        break                 
