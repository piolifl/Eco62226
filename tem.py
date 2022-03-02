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
ccl = 0
mep = 0
peso = 0

tipo = {'al':['30'],'aap':['L'],'k':['O'],'s31m':['2']

#'gd':['30'],'al':['30','29','35','41'],'ae':['38'],'gd':['30','29','35','38','41','46'],'aap':['L'],'k':['O']
}
plazo = ['CI',#'48hs','24hs'
]
moneda = {
    'ccl|mep':['C','D'],#  'mep|ccl':['D','C'],'mep|pes':['D',''],'ccl|pes':['C','']
}
nominal = [200,5]

def bid_ask(a,b,bb,aa):
    
    pass

def calcular(tickerA,vA,tickerB,cB,vB,cA):
    global comA
    if tickerA == 'aap' or tickerA == 'k':  venA = round(vA * (1-costos),2) * nominal[1]
    else: venA = round((vA/100) * (1-costos),2) * nominal[0]
    if tickerB == 'aap' or tickerB == 'k': comB = venA // round(cB * (1+costos),2)
    else: comB = venA // round((cB/100) * (1+costos),2)
    if tickerB == 'aap' or tickerB == 'k':  venB = round(vB * (1-costos),2) * comB
    else:  venB = comB * round((vB/100) * (1-costos),2)
    if tickerA == 'aap' or tickerA == 'k':  comA = venB // round(cA * (1+costos),2)
    else: comA = venB // round((cA/100) * (1+costos),2)
    return comA

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
                            if clave == cla: continue
                            while True:
                                vendoA =   pr.precioBI( 'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' + u )
                                comproB =  pr.precioOF( 'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u )
                                vendoB =   pr.precioBI( 'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u )
                                comproA =  pr.precioOF( 'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' + u )

                                #if vendoA == 1000 or comproB == 1000 or vendoB == 1000 or comproA == 1000: break

                                calcular(clave,vendoA,cla,comproB,vendoB,comproA)

                                res = comA - nominal[0]

                                if clave != 'aap' or clave != 'k': uso = nominal[0] 
                                else: uso = nominal[1]
                                if comA > uso + 1000000:
                                    if   pr.bidsBI(     'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' + u ) < valor[1]: continue
                                    elif pr.offersOF(   'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u  ) < comproB:  continue
                                    elif pr.bidsBI(     'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u  ) < comproB:  continue
                                    elif pr.offersOF(   'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' + u ) < comproA:  continue

                                    print('GANA' + clave.upper() + a + i[0] + '-' + u + ' '+ str(vendoA) + '|', end=' ')
                                    print(cla.upper() + aa + i[0] + '-' + u + ' ' + str(comproB)+ '|', end=' ')
                                    print(cla.upper() + aa + i[1] + '-' + u + ' ' + str(vendoB)+ '|', end=' ')
                                    print(clave.upper() + a + i[1] + '-' + u + ' '+ str(comproA) + '|' + str(res) +' || '+str(gana))
                                    gana += res
                                    continue
                                else:
                                    print(  '| NO |' + clave.upper() + a + i[0] + '-' + u + ' '+ str(vendoA) + '|', end=' ')
                                    print(cla.upper() + aa + i[0] + '-' + u + ' ' + str(comproB)+ '|', end=' ')
                                    print(cla.upper() + aa + i[1] + '-' + u + ' ' + str(vendoB)+ '|', end=' ')
                                    print(clave.upper() + a + i[1] + '-' + u + ' '+ str(comproA) + '|' + 'RESULTA: ' + str(res)+' || ' +str(gana))
                                    break







