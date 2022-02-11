from Consultar import Consultar
from Operar import Operar
from datetime import datetime
import math
import time

pr = Consultar()
op = Operar()

costos = 0.0026
limite = 1000
gana = 0
bono = 0
ccl = 0
mep = 0
peso = 0

moneda = {
    'ccl-mep':['C','D'],  'mep-ccl':['D','C'], #'mep-pes':['D',''] , 'ccl-pes':['C','']
}

plazo = ['CI','48hs',#'24hs'
]

par = { 
    '1':['al30',200,'gd30'],'2':['gd30',200,'al30'],

    '10':['al30',200,'ae38'],   '11':['al30',200,'al29'],   '12':['al30',200,'al35'],   '13':['al30',200,'al41'],
    '14':['ae38',200,'al30'],   '15':['ae38',200,'al29'],   '16':['ae38',200,'al35'],   '17':['ae38',200,'al41'],
    '18':['al29',200,'al30'],   '19':['al29',200,'ae38'],   '20':['al29',200,'al35'],   '21':['al29',200,'al41'],
    '22':['al35',200,'al30'],   '23':['al35',200,'ae38'],   '24':['al35',200,'al29'],   '25':['al35',200,'al41'],
    '26':['al41',200,'al30'],   '27':['al41',200,'ae38'],   '28':['al41',200,'al29'],   '29':['al41',200,'al35'],

    '30':['al30',200,'gd29'],   '31':['al30',200,'gd30'],   '32':['al30',200,'gd35'],   '33':['al30',200,'gd38'],   '34':['al30',200,'gd41'],   '35':['al30',200,'gd46'],
    '36':['ae38',200,'gd29'],   '37':['ae38',200,'gd30'],   '38':['ae38',200,'gd35'],   '39':['ae38',200,'gd38'],   '40':['ae38',200,'gd41'],   '41':['ae38',200,'gd46'],
    '42':['al29',200,'gd29'],   '43':['al29',200,'gd30'],   '44':['al29',200,'gd35'],   '45':['al29',200,'gd38'],   '46':['al29',200,'gd41'],   '47':['al29',200,'gd46'],
    '48':['al35',200,'gd29'],   '49':['al35',200,'gd30'],   '50':['al35',200,'gd35'],   '51':['al35',200,'gd38'],   '52':['al35',200,'gd41'],   '53':['al35',200,'gd46'],
    '54':['al41',200,'gd29'],   '55':['al41',200,'gd30'],   '56':['al41',200,'gd35'],   '57':['al41',200,'gd38'],   '58':['al41',200,'gd41'],   '59':['al41',200,'gd46'],

    '60':['al30',200,'s28f2'],  '61':['al30',200,'s31m2'],
    
    '70':['al30',200,'aapl'],'71':['al30',200,'ko'],
    '80':['al30',200,'s28f2'],'81':['al30',200,'s31m2'],

    '100.1':['al30',200,'gd30'],'101.1':['gd30',200,'al30'],
 
    '100':['gd30',200,'gd29'],  '101':['gd30',200,'gd35'],  '102':['gd30',200,'gd38'],  '103':['gd30',200,'gd41'],  '104':['gd30',200,'gd46'],
    '105':['gd29',200,'gd30'],  '106':['gd29',200,'gd35'],  '107':['gd29',200,'gd38'],  '108':['gd29',200,'gd41'],  '109':['gd29',200,'gd46'],
    '110':['gd35',200,'gd30'],  '111':['gd35',200,'gd29'],  '112':['gd35',200,'gd38'],  '113':['gd35',200,'gd41'],  '114':['gd35',200,'gd46'],
    '115':['gd38',200,'gd30'],  '116':['gd38',200,'gd29'],  '117':['gd38',200,'gd35'],  '118':['gd38',200,'gd41'],  '119':['gd38',200,'gd46'],
    '120':['gd41',200,'gd30'],  '121':['gd41',200,'gd29'],  '122':['gd41',200,'gd35'],  '123':['gd41',200,'gd38'],  '124':['gd41',200,'gd46'],
    '125':['gd46',200,'gd30'],  '126':['gd46',200,'gd29'],  '127':['gd46',200,'gd35'],  '128':['gd46',200,'gd38'],  '129':['gd46',200,'gd41'],

    '130':['gd30',200,'ae38'],  '131':['gd30',200,'al29'],  '132':['gd30',200,'al30'],  '133':['gd30',200,'al35'],  '134':['gd30',200,'al41'],
    '135':['gd29',200,'ae38'],  '136':['gd29',200,'al29'],  '137':['gd29',200,'al30'],  '138':['gd29',200,'al35'],  '139':['gd29',200,'al41'],
    '140':['gd35',200,'ae38'],  '141':['gd35',200,'al29'],  '142':['gd35',200,'al30'],  '143':['gd35',200,'al35'],  '144':['gd35',200,'al41'],
    '145':['gd38',200,'ae38'],  '146':['gd38',200,'al29'],  '147':['gd38',200,'al30'],  '148':['gd38',200,'al35'],  '149':['gd38',200,'al41'],
    '150':['gd41',200,'ae38'],  '151':['gd41',200,'al29'],  '152':['gd41',200,'al30'],  '153':['gd41',200,'al35'],  '154':['gd41',200,'al41'],
    '155':['gd46',200,'ae38'],  '156':['gd46',200,'al29'],  '157':['gd46',200,'al30'],  '158':['gd46',200,'al35'],  '159':['gd46',200,'al41'],

    '170':['gd30',200,'aapl'],'171':['gd30',200,'ko'],
    '180':['gd30',200,'s28f2'],'181':['gd30',200,'s31m2'],


    '200':['s28f2',8000,'al30'], '201':['s28f2',8000,'gd30'],'202':['s28f2',8000,'aapl'],'203':['s28f2',8000,'ko'],'204':['s28f2',8000,'s31m2'],

    '300':['aapl',5,'al30'],'301':['aapl',5,'gd30'],'302':['aapl',5,'ko'],'303':['aapl',5,'s28f2'],'304':['aapl',5,'s31m2'],
    '400':['ko',5,'al30'],'401':['ko',5,'gd30'],'402':['ko',5,'aapl'],'403':['ko',5,'s28f2'],'404':['ko',5,'s31m2']

        }

def ganaMoneda(mon,a,b):
    global ccl, mep, peso
    if mon == 'ccl-mep':
        if a == 'aapl' or a == 'ok':
            ccl += round(vendoA - comproB * pr_comproB/100,2)
            mep += round(vendoB - comproA * pr_comproA,2)
        elif b == 'aapl' or b == 'ok':
            ccl += round(vendoA - comproB * pr_comproB,2)
            mep += round(vendoB - comproA * pr_comproA/100,2)
        else:
            ccl += round(vendoA - comproB * pr_comproB/100,2)
            mep += round(vendoB - comproA * pr_comproA/100,2)
    elif mon == 'mep-ccl':
        if a == 'aapl' or a == 'ok':
            mep += round(vendoA - comproB * pr_comproB/100,2)
            ccl += round(vendoB - comproA * pr_comproA,2)
        elif b == 'aapl' or b == 'ok':
            mep += round(vendoA - comproB * pr_comproB,2)
            ccl += round(vendoB - comproA * pr_comproA/100,2)
        else:
            mep += round(vendoA - comproB * pr_comproB/100,2)
            ccl += round(vendoB - comproA * pr_comproA/100,2)
    elif mon == 'ccl-pes':
        if a == 'aapl' or a == 'ok':
            ccl  += round(vendoA - comproB * pr_comproB/100,2)
            peso += round(vendoB - comproA * pr_comproA,2)
        elif b == 'aapl' or b == 'ok':
            ccl  += round(vendoA - comproB * pr_comproB,2)
            peso += round(vendoB - comproA * pr_comproA/100,2)
        else:
            ccl  += round(vendoA - comproB * pr_comproB/100,2)
            peso += round(vendoB - comproA * pr_comproA/100,2)
    elif mon == 'mep-pes':
        if a == 'aapl' or a == 'ok':
            mep  += round(vendoA - comproB * pr_comproB/100,2)
            peso += round(vendoB - comproA * pr_comproA,2)
        elif b == 'aapl' or b == 'ok':
            mep  += round(vendoA - comproB * pr_comproB,2)
            peso += round(vendoB - comproA * pr_comproA/100,2)
        else:
            mep  += round(vendoA - comproB * pr_comproB/100,2)
            peso += round(vendoB - comproA * pr_comproA/100,2)

while True:
    if time.strftime("%H:%M:%S") < '11:00:00':
        print('Esperando la apertura ...', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),time.sleep(10)
        continue
    if time.strftime("%H:%M:%S") > '16:59:50':
        print(f'FIN 17hs CERRADO | lim{limite} | {valor[0].upper()}: {gana} | >>> ccl {ccl} mep {mep} pesos {peso}')
        break
    if time.strftime("%H:%M:%S") > '15:59:45': plazo = ['48hs','24hs']

    for clave,valor in par.items():
        if limite < 200: 
            if valor[0] == 'al30' or valor[2] == 'al30': continue

        for e,i in moneda.items():
            for u in plazo:
                while True:
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
                    gana = comproA - valor[1]
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

                        ganaMoneda(e,valor[0],valor[2])

                        bono += comproA - valor[1]

                        print(time.strftime("%H:%M:%S"),f' | SI | {e} {valor[0].upper()} {valor[2].upper()} {u} |  limite {limite} | {valor[0].upper()}: {bono} | >>> ccl {ccl} mep {mep} pesos {peso}')

                        pr.logRulos(str(e)+ ' | ' + str(valor[0].upper())+ ': ' + str(bono) + ' | >>> ccl: ' + str(ccl) + ' mep: ' + str(mep) + ' pesos: ' + str(peso))

                        if valor[0] == 'al30' or valor[2] == 'al30': limite -= valor[1] 
                        continue                         
                    else: 
                        print(time.strftime("%H:%M:%S"),f'| NO | {gana} | {e} {valor[0].upper()} {valor[2].upper()} {u} | limite: {limite} | {valor[0].upper()}: {bono} | >>> ccl: {ccl} mep: {mep} pesos: {peso}')
                        break       
