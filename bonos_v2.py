
from Consultar import Consultar
from Operar import Operar
from datetime import datetime
import math
import time

pr = Consultar()
op = Operar()

costos = 0.0026
limite = 2000
gana = 0
ccl = 0
mep = 0
pes = 0

tipo = {'al':['30'],'gd':['30','35'],
#'al':['30','29','35','41'],'ae':['38'],'gd':['30','29','35','38','41','46'],'aap':['L'],'k':['O'],'amz':['N']
}
plazo = ['CI',
'48hs',#'24hs'
]
moneda = {
'ccl|mep':['C','D'],'mep|ccl':['D','C'],
'mep|pes':['D',''],'ccl|pes':['C','']
}
nominal = [1000,2]

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
            ccl += round(venA - comB * comproB/100,2)
            mep += round(venB - comA * comproA,2)
        elif tickerB == 'aap' or tickerB == 'k' or tickerB == 'amz':
            ccl += round(venA - comB * comproB,2)
            mep += round(venB - comA * comproA/100,2)
        else:
            ccl += round(venA - comB * comproB/100,2)
            mep += round(venB - comA * comproA/100,2)
    elif tipo == 'mep|ccl':
        if tickerA == 'aap' or tickerA == 'k' or tickerA == 'amz':
            mep += round(venA - comB * comproB/100,2)
            ccl += round(venB - comA * comproA,2)
        elif tickerB == 'aap' or tickerB == 'k' or tickerB == 'amz':
            mep += round(venA - comB * comproB,2)
            ccl += round(venB - comA * comproA/100,2)
        else:
            mep += round(venA - comB * comproB/100,2)
            ccl += round(venB - comA * comproA/100,2)
    elif tipo == 'ccl|pes':
        if tickerA == 'aap' or tickerA == 'k' or tickerA == 'amz':
            ccl  += round(venA - comB * comproB/100,2)
            pes += round(venB - comA * comproA,2)
        elif tickerB == 'aap' or tickerB == 'k' or tickerB == 'amz':
            ccl  += round(venA - comB * comproB,2)
            pes += round(venB - comA * comproA/100,2)
        else:
            ccl  += round(venA - comB * comproB/100,2)
            pes += round(venB - comA * comproA/100,2)
    elif tipo == 'mep|pes':
        if tickerA == 'aap' or tickerA == 'k' or tickerA == 'amz':
            mep  += round(venA - comB * comproB/100,2)
            pes += round(venB - comA * comproA,2)
        elif tickerB == 'aap' or tickerB == 'k' or tickerB == 'amz':
            mep  += round(venA - comB * comproB,2)
            pes += round(venB - comA * comproA/100,2)
        else:
            mep  += round(venA - comB * comproB/100,2)
            pes += round(venB - comA * comproA/100,2)

while True:
    if time.strftime("%H:%M:%S") < '11:00:00':
        print('Esperando la apertura ...', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),time.sleep(10)
        continue
    if time.strftime("%H:%M:%S") > '16:59:50':
        print(f'FIN 17hs CERRADO |')
        break
    if time.strftime("%H:%M:%S") > '15:59:45': plazo = ['48hs','24hs']
    for clave, valor in tipo.items():
        for a in valor:
            for e,i in moneda.items():
                for u in plazo:
                    for cla,val in tipo.items():
                        for aa in val:
                            if (clave + a) == (cla + aa): continue
                            while True:
                                if limite < 200 and ((clave + a) == 'al30' or (cla + aa) == 'al30') : break
                                #LAST
                                vendoA=  pr.precioLA( 'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' +u)
                                comproB= pr.precioLA( 'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u)
                                vendoB=  pr.precioLA( 'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u)
                                comproA= pr.precioLA( 'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' +u)
                                #BID-OFFER
                                '''vendoA =   pr.precioBI( 'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' + u)
                                comproB =  pr.precioOF( 'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u )
                                vendoB =   pr.precioBI( 'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u )
                                comproA =  pr.precioOF( 'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' + u )'''
                                #print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                if vendoA == 10000 or comproB == 10000 or vendoB == 10000 or comproA == 10000: break

                                cruzar(clave,cla,vendoA,comproB,vendoB,comproA)
                                
                                if clave == 'aap' or clave == 'k' or clave == 'amz': 
                                    uso = nominal[1] 
                                    res = comA - nominal[1]
                                else: 
                                    uso = nominal[0]
                                    res = comA - nominal[0]

                                if comA >= uso:

                                    if pr.bidsBI('MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' + u ) < uso: break
                                    elif pr.offersOF('MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u ) < comproB:  break
                                    elif pr.bidsBI('MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u ) < comproB:  break
                                    elif pr.offersOF('MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' + u ) < comproA:  break

                                    #op.vender   ( ( 'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' + u ) , uso , vendoA )
                                    #op.comprar  ( ( 'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u)   , comB, comproB )
                                    #op.vender   ( ( 'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u )  , comB, vendoB )
                                    #op.comprar  ( ( 'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' + u ) , comA, comproA )

                                    print('| SI |' + clave.upper() + a + i[0] + '-' + u + ' '+ str(vendoA) + '|', end=' ')
                                    print(cla.upper() + aa + i[0] + '-' + u + ' ' + str(comproB )+ '|', end=' ')
                                    print(cla.upper() + aa + i[1] + '-' + u + ' ' + str(vendoB)+ '|', end=' ')
                                    print(clave.upper() + a + i[1] + '-' + u + ' '+ str(comproA) + '| lim: '+ str(limite) + '| RES: ' + str(round(res,2))+' | ' +str(gana) + ' | '+ str(ccl)+' | '+str(mep)+' | '+ str(pes))

                                    resultado(e,clave,cla)
                                    if (clave + a) == 'al30' or (cla + aa) == 'al30': limite -= nominal[0]
                                    gana += res
                                    if time.strftime("%H:%M:%S") > '15:59:45': plazo = ['48hs','24hs']
                                    continue

                                else:
                                    print('|'+clave.upper()+a+i[0]+u.lower()+''+str(vendoA)+'x'+str(uso)+'= $'+str(venA)+'|',end=' ')
                                    print(cla.upper()+aa+i[0]+u.lower()+''+str(comproB)+'/$'+str(venA)+'= '+str(comB)+'|',end=' ') 
                                    print(cla.upper()+aa+i[1]+u.lower()+''+str(vendoB)+'x'+str(comB)+'= $'+str(round(venB*(comB/100),2) )+'|', end=' ') 
                                    print(clave.upper()+a+i[1]+u.lower()+' '+str(comA)+'|'+str(limite)+'|'+str(round(gana,2))+'|'+str(round(ccl,2))+'|'+str(round(mep,2))+'|'+ str(round(pes,2)))

                                    break

