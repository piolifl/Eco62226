
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
s31e2 = 0
ccl = 0
mep = 0
peso = 0

moneda = {'ccl-mep':['C','D'],  'mep-ccl':['D','C'],  'mep-pes':['D',''] , 'ccl-pes':['C','']}

plazo = ['CI  ','48hs','24hs']

par = { '1':['al30',200,'gd30'], '2':['al30',200,'s31e2'],'3':['al30',200,'aapl'],
        '10':['gd30',200,'al30'], '11':['gd30',200,'s31e2'],'12':['gd30',200,'aapl'],
        '20':['s31e2',8000,'al30'], '21':['s31e2',8000,'gd30'],'22':['s31e2',8000,'aapl'],
        '30':['aapl',5,'al30'], '31':['aapl',5,'gd30'], '30':['aapl',5,'s31e2']           
        }

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
        print(f'FIN 17hs CERRADO | lim{limite} | al30 {al30} | gd30 {gd30} | s31e2 {s31e2} | aapl {aapl} | ko {ko} | >>> ccl {ccl} mep {mep} pesos {peso} ')
        break
    if limite < 200: 
        print(f'FIN LIMITE AGOTADO | lim{limite} | al30 {al30} | gd30 {gd30} | s31e2 {s31e2} | aapl {aapl} | ko {ko} | >>> ccl {ccl} mep {mep} pesos {peso}  ')
        break  
    for clave,valor in par.items():
        for e,i in moneda.items():
            for u in plazo:
                if time.strftime("%H:%M:%S") > '15:59:45': plazo = ['48hs','24hs']
                pr_vendoA =   pr.precioBI( 'MERV - XMEV - ' + valor[0].upper() + i[0] + ' - ' + u )
                pr_comproB =  pr.precioOF( 'MERV - XMEV - ' + valor[2].upper() + i[0] + ' - ' + u )
                pr_vendoB =   pr.precioBI( 'MERV - XMEV - ' + valor[2].upper() + i[1] + ' - ' + u )
                pr_comproA =  pr.precioOF( 'MERV - XMEV - ' + valor[0].upper() + i[1] + ' - ' + u )
                if pr_vendoA == 1000 or pr_comproB == 1000 or pr_vendoB == 1000 or pr_comproA == 1000: continue

                if valor[0] == 'aapl' or valor[0] == 'ko': vendoA = round(pr_vendoA * (1-costos),2) * valor[1]
                else: vendoA = round((pr_vendoA/100) * (1-costos),2) * valor[1]
                if valor[2] == 'aapl' or valor[2] == 'ko': comproB = vendoA // round(pr_comproB * (1+costos),2)
                else: comproB = vendoA // round((pr_comproB/100) * (1+costos),2)
                if valor[2] == 'aapl' or valor[2] == 'ko': vendoB = round(pr_vendoB * (1-costos),2) * comproB
                else: vendoB = comproB * round((pr_vendoB/100) * (1-costos),2)
                if valor[0] == 'aapl' or valor[0] == 'ko': comproA = vendoB // round(pr_comproA * (1+costos),2)
                else: comproA = vendoB // round((pr_comproA/100) * (1+costos),2)

                if comproA > valor[1]: 

                    if   valor[0] == 'al30':   al30 = int(comproA - valor[1])
                    elif valor[0] == 'gd30':   gd30 = int(comproA - valor[1])
                    elif valor[0] == 'aapl':   aapl = int(comproA - valor[1])
                    elif valor[0] == 'ko':       ko = int(comproA - valor[1])
                    elif valor[0] == 's31e2': s31e2 = int(comproA - valor[1])

                    ganaMoneda(i)

                    #op.vender   ( ( 'MERV - XMEV - ' + valor[0].upper() + i[0] + ' - ' + u )   , e[1],       pr_vendoA )
                    #op.comprar  ( ( 'MERV - XMEV - ' + valor[2].upper() + i[0] + ' - ' + u )   , comproB,    pr_comproB )
                    #op.vender   ( ( 'MERV - XMEV - ' + valor[2].upper() + i[1] + ' - ' + u )   , comproB,    pr_vendoB )
                    #op.comprar  ( ( 'MERV - XMEV - ' + valor[0].upper() + i[1] + ' - ' + u )   , comproA,    pr_comproA )


                    print(time.strftime("%H:%M:%S"),f' | SI | {e} {valor[0]} {valor[2]} {u} |  limite {limite} | al30 {al30} | gd30 {gd30} | s31e2 {s31e2} | aapl {aapl} | ko {ko} | >>> ccl {ccl} mep {mep} pesos {peso}  ')

                    pr.logRulos('Entre: ' + str(e) + 'AL30: ' + str(al30) + ' | GD30: ' + str(gd30) + ' | S31E2: ' + str(s31e2) + ' | AAPL: ' + str(aapl) + ' | KO: ' + str(ko) + '| >>> ccl ' + str(ccl) + ' mep ' + str(mep) + ' pesos ' + str(peso) )

                    continue
                        
                else: print(time.strftime("%H:%M:%S"),f' | NO | {comproA} | {e} {valor[0]} {valor[2]} {u} | limite {limite} | al30 {al30} | gd30 {gd30} | s31e2 {s31e2} | aapl {aapl} | ko {ko} | >>> ccl {ccl} mep {mep} pesos {peso}  ')
