
from Consultar import Consultar
from Operar import Operar
from datetime import datetime
import math
import time

pr = Consultar()
op = Operar()

costos = 0.0026
limite = 1000000
gana = 0
ccl = 0
mep = 0
pes = 0
bonos = {'al30':0,'gd30':0,'gd35':0}

tipo = {'al':['30'],'gd':['35','30'],
#'al':['30','29','35','41'],'ae':['38'],'gd':['30','29','35','38','41','46'],'aap':['L'],'k':['O'],'amz':['N']
}
plazo = ['CI',
'48hs','24hs'
]
moneda = {
'ccl|mep':['C','D'],'mep|ccl':['D','C'],
#'mep|pes':['D',''],'ccl|pes':['C','']
}
nominal = [25,2]

def cruzar(tickerA,tickerB,vendo1,compro2,vendo2,compro1):
    global comA,comB,venA,venB
    if tickerA == 'aap' or tickerA == 'k' or tickerA == 'amz' : venA = round(vendo1 * nominal[1] * (1-costos),2)
    else: venA = round((vendo1/100) * nominal[0] * (1-costos),2)
    if tickerB == 'aap' or tickerB == 'k' or tickerB == 'amz': comB = venA // (compro2 * (1+costos))
    else: comB = venA // ((compro2/100) * (1+costos))
    if tickerB == 'aap' or tickerB == 'k' or tickerB == 'amz': venB = round( comB * vendo2 * (1-costos),2)
    else: venB = round( comB * (vendo2/100) * (1-costos),2)
    if tickerA == 'aap' or tickerA == 'k' or tickerA == 'amz': comA = venB // (compro1 * (1+costos))
    else:comA = venB // ((compro1/100) * (1+costos))
def resultado(tipo,tickerA,tickerB):
    global ccl,mep,pes
    if tipo == 'ccl|mep':
        if tickerA == 'aap' or tickerA == 'k' or tickerA == 'amz':
            ccl += round(venA - comB * comproB[0]/100,2)
            mep += round(venB - comA * comproA[0],2)
        elif tickerB == 'aap' or tickerB == 'k' or tickerB == 'amz':
            ccl += round(venA - comB * comproB[0],2)
            mep += round(venB - comA * comproA[0]/100,2)
        else:
            ccl += round(venA - comB * comproB[0]/100,2)
            mep += round(venB - comA * comproA[0]/100,2)
    elif tipo == 'mep|ccl':
        if tickerA == 'aap' or tickerA == 'k' or tickerA == 'amz':
            mep += round(venA - comB * comproB[0]/100,2)
            ccl += round(venB - comA * comproA[0],2)
        elif tickerB == 'aap' or tickerB == 'k' or tickerB == 'amz':
            mep += round(venA - comB * comproB[0],2)
            ccl += round(venB - comA * comproA[0]/100,2)
        else:
            mep += round(venA - comB * comproB[0]/100,2)
            ccl += round(venB - comA * comproA[0]/100,2)
    elif tipo == 'ccl|pes':
        if tickerA == 'aap' or tickerA == 'k' or tickerA == 'amz':
            ccl  += round(venA - comB * comproB[0]/100,2)
            pes += round(venB - comA * comproA[0],2)
        elif tickerB == 'aap' or tickerB == 'k' or tickerB == 'amz':
            ccl  += round(venA - comB * comproB[0],2)
            pes += round(venB - comA * comproA[0]/100,2)
        else:
            ccl  += round(venA - comB * comproB[0]/100,2)
            pes += round(venB - comA * comproA[0]/100,2)
    elif tipo == 'mep|pes':
        if tickerA == 'aap' or tickerA == 'k' or tickerA == 'amz':
            mep  += round(venA - comB * comproB[0]/100,2)
            pes += round(venB - comA * comproA[0],2)
        elif tickerB == 'aap' or tickerB == 'k' or tickerB == 'amz':
            mep  += round(venA - comB * comproB[0],2)
            pes += round(venB - comA * comproA[0]/100,2)
        else:
            mep  += round(venA - comB * comproB[0]/100,2)
            pes += round(venB - comA * comproA[0]/100,2)

while True:
    if time.strftime("%H:%M:%S") < '11:00:00':
        print('Esperando la apertura ...', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),time.sleep(10)
        continue
    if time.strftime("%H:%M:%S") > '16:59:50':
        print(f'FIN 17hs CERRADO |')
        break
    if time.strftime("%H:%M:%S") > '15:59:45': plazo = ['48hs','24hs']
    for clave, valor in tipo.items():
        if time.strftime("%H:%M:%S") > '16:59:50': break
        if time.strftime("%H:%M:%S") > '15:59:45': plazo = ['48hs','24hs']
        for a in valor:
            for e,i in moneda.items():
                for u in plazo:
                    for cla,val in tipo.items():
                        for aa in val:
                            if (clave + a) == (cla + aa): continue
                            while True:
                                if limite < 200 and ((clave + a) == 'al30' or (cla + aa) == 'al30') : break
                                #LAST
                                vendoA = pr.precioLA( 'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' +u)
                                comproB= pr.precioLA( 'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u)
                                vendoB = pr.precioLA( 'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u)
                                comproA= pr.precioLA( 'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' +u)
                                #BID-OFFER
                                '''vendoA =   pr.precioBI( 'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' + u)
                                comproB =  pr.precioOF( 'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u )
                                vendoB =   pr.precioBI( 'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u )
                                comproA =  pr.precioOF( 'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' + u )'''
                                print(f'Buscando...{u} | {clave.upper()}{a} | {cla.upper()}{aa} |',datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                if vendoA[0] == 10000 or comproB[0] == 10000 or vendoB[0] == 10000 or comproA[0] == 10000: break

                                cruzar(clave,cla,vendoA[0],comproB[0],vendoB[0],comproA[0])
                                
                                if clave == 'aap' or clave == 'k' or clave == 'amz': 
                                    uso = nominal[1] 
                                    res = comA - nominal[1]
                                else: 
                                    uso = nominal[0]
                                    res = comA - nominal[0]
                                
                                if comA >= uso:
                                    #last - bid/off    
                                    if vendoA[1] <= uso: break
                                    elif comproB[2] <= comB: break
                                    elif vendoB[1] <= comB:  break
                                    elif comproA[2] <= comA:  break
                                    #PUNTAS: bid/off
                                    '''if vendoA[1] <= uso: break
                                    elif comproB[1] <= comB: break
                                    elif vendoB[1] <= comB: break
                                    elif comproA[1] <= comA: break'''

                                    #op.vender   ( ( 'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' + u ) , uso , vendoA[0] )
                                    #op.comprar  ( ( 'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u)   , comB, comproB[0] )
                                    #op.vender   ( ( 'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u )  , comB, vendoB[0] )
                                    #op.comprar  ( ( 'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' + u ) , comA, comproA[0] )

                                    for bonos_clave, bonos_valor in bonos.items():
                                        if bonos_clave == clave+a: bonos_clave += res

                                    print(' SI ' + clave.upper() + a + i[0] + '-' + u + ' '+ str(vendoA[0])+'|', end='')
                                    print(cla.upper() + aa + i[0] + '-' + u + ' ' + str(comproB[0] )+ '|', end='')
                                    print(cla.upper() + aa + i[1] + '-' + u + ' ' + str(vendoB[0])+ '|', end='')
                                    print(clave.upper() + a + i[1] + '-' + u + ' '+ str(comproA[0])+'|lim:'+ str(limite)+'|RES:'+str(round(res,2))+'|' +str(gana)+'|ccl:'+str(round(ccl,2))+'|usd:'+str(round(mep,2))+'|ars:'+str(round(pes,2))+bonos)

                                    resultado(e,clave,cla)
                                    if (clave + a) == 'al30' or (cla + aa) == 'al30': limite -= nominal[0]
                                    gana += res
                                    continue
                                else:
                                    print('|'+clave.upper()+a+i[0]+u.lower()+''+str(vendoA[0])+'x'+str(uso)+'=$'+str(venA)+'|',end='')
                                    print(cla.upper()+aa+i[0]+u.lower()+''+str(comproB[0])+'/$'+str(venA)+'='+str(comB)+'|',end='') 
                                    print(cla.upper()+aa+i[1]+u.lower()+''+str(vendoB[0])+'x'+str(comB)+'=$'+str(round(venB*(comB/100),2) )+'|', end='') 
                                    print(clave.upper()+a+i[1]+u.lower()+' '+str(comA)+'|'+str(limite)+'|'+str(round(gana,2))+'|'+str(round(ccl,2))+'|'+str(round(mep,2))+'|'+ str(round(pes,2))+bonos)

                                    break


