from Consultar import Consultar
from Operar import Operar
from datetime import datetime
import math
import time

while True:
    if time.strftime("%H:%M:%S") < '11:00:00':
        print('Esperando la apertura ...', datetime.now().strftime("%H:%M:%S  %d/%m/%Y")),time.sleep(10)
        continue
    else: break

pr = Consultar()
op = Operar()

costos = 0.0026
limite = 100000
gana = 0
ccl = 0
mep = 0
pes = 0
bonos = {}

tipo = {'al':['30'],'gd':['35','30'], 
's30j':['2'], #'s31g':['2'], #'s30s':['2'], #'s31o':['2'],
#'aap':['L'], #'k':['O'], #'amz':['N'],
#'al':['30','29','35','41'],'ae':['38'],'gd':['30','29','35','38','41','46']
}
plazo = ['CI',
'48hs', '24hs'
]
moneda = {
'ccl|mep':['C','D'],
'mep|ccl':['D','C'],
#'mep|pes':['D',''],
#'ccl|pes':['C','']
}
nominal = [26,2,1500]

def cruzar(tA,tB,vendo1,compro2,vendo2,compro1):
    global comA,comB,venA,venB
    if tA=='aap' or tA=='k' or tA=='amz': venA = round(vendo1 * nominal[1] * (1-costos),2)
    elif tA=='s30j' or tA=='s31g': venA = round((vendo1/100) * nominal[2] * (1-costos),2)
    else: venA = round((vendo1/100) * nominal[0] * (1-costos),2)
    if tB=='aap' or tB=='k' or tB=='amz': comB = venA // (compro2 * (1+costos))
    else: comB = venA // ((compro2/100) * (1+costos))
    if tB=='aap' or tB=='k' or tB=='amz': venB = round( comB * vendo2 * (1-costos),2)
    else: venB = round( comB * (vendo2/100) * (1-costos),2)
    if tA=='aap' or tA=='k' or tA=='amz': comA = venB // (compro1 * (1+costos))
    else:comA = venB // ((compro1/100) * (1+costos))
def resultado(tipo,tA,tB):
    global ccl,mep,pes
    if tipo == 'ccl|mep':
        if tA=='aap' or tA=='k' or tA=='amz':
            ccl += round(venA - comB * comproB[0]/100,2)
            mep += round(venB - comA * comproA[0],2)
        elif tB=='aap' or tB=='k' or tB=='amz':
            ccl += round(venA - comB * comproB[0],2)
            mep += round(venB - comA * comproA[0]/100,2)
        else:
            ccl += round(venA - comB * comproB[0]/100,2)
            mep += round(venB - comA * comproA[0]/100,2)
    elif tipo == 'mep|ccl':
        if tA=='aap' or tA=='k' or tA=='amz':
            mep += round(venA - comB * comproB[0]/100,2)
            ccl += round(venB - comA * comproA[0],2)
        elif tB=='aap' or tB=='k' or tB=='amz':
            mep += round(venA - comB * comproB[0],2)
            ccl += round(venB - comA * comproA[0]/100,2)
        else:
            mep += round(venA - comB * comproB[0]/100,2)
            ccl += round(venB - comA * comproA[0]/100,2)
    elif tipo == 'ccl|pes':
        if tA=='aap' or tA=='k' or tA=='amz':
            ccl  += round(venA - comB * comproB[0]/100,2)
            pes += round(venB - comA * comproA[0],2)
        elif tB=='aap' or tB=='k' or tB=='amz':
            ccl  += round(venA - comB * comproB[0],2)
            pes += round(venB - comA * comproA[0]/100,2)
        else:
            ccl  += round(venA - comB * comproB[0]/100,2)
            pes += round(venB - comA * comproA[0]/100,2)
    elif tipo == 'mep|pes':
        if tA=='aap' or tA=='k' or tA=='amz':
            mep  += round(venA - comB * comproB[0]/100,2)
            pes += round(venB - comA * comproA[0],2)
        elif tB=='aap' or tB=='k' or tB=='amz':
            mep  += round(venA - comB * comproB[0],2)
            pes += round(venB - comA * comproA[0]/100,2)
        else:
            mep  += round(venA - comB * comproB[0]/100,2)
            pes += round(venB - comA * comproA[0]/100,2)

while True:
    if time.strftime("%H:%M:%S") > '17:59:50':
        print(f'FIN 17hs CERRADO |', datetime.now().strftime("%H:%M:%S  %d/%m/%Y"))
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
                                #Limite de uso para el AL30
                                if limite < 25 and ((clave + a) == 'al30' or (cla + aa) == 'al30') : break

                                #Consulto precios LAST
                                if (clave=='s30j' or clave=='s31g') and (i[0]=='C' or i[0]=='D'): vendoA = pr.precioLA('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[0]+' - '+u)
                                else: vendoA = pr.precioLA( 'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' +u)
                                if (cla=='s30j' or cla=='s31g') and (i[0]=='C' or i[0]=='D'): comproB= pr.precioLA('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[0]+' - '+u)
                                else: comproB= pr.precioLA( 'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u)
                                if (cla=='s30j' or cla=='s31g') and (i[1]=='C' or i[1]=='D'): vendoB = pr.precioLA('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[1]+' - '+u)
                                else: vendoB = pr.precioLA( 'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u)
                                if (clave=='s30j' or clave=='s31g') and (i[1]=='C' or i[1]=='D'): comproA= pr.precioLA('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[1]+' - '+u)
                                else: comproA= pr.precioLA( 'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' +u)

                                #Consulto precios PUNTAS 
                                '''if (clave=='s30j' or clave=='s31g') and (i[0]=='C' or i[0]=='D'): vendoA = pr.precioBI('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[0]+' - '+u)
                                else: vendoA = pr.precioBI( 'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' +u)
                                if (cla=='s30j' or cla=='s31g') and (i[0]=='C' or i[0]=='D'): comproB= pr.precioOF('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[0]+' - '+u)
                                else: comproB= pr.precioOF( 'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u)
                                if (cla=='s30j' or cla=='s31g') and (i[1]=='C' or i[1]=='D'): vendoB = pr.precioBI('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[1]+' - '+u)
                                else: vendoB = pr.precioBI( 'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u)
                                if (clave=='s30j' or clave=='s31g') and (i[1]=='C' or i[1]=='D'): comproA= pr.precioOF('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[1]+' - '+u)
                                else: comproA= pr.precioOF( 'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' +u)'''
                                
                                print(f'Buscando... {u} | {clave.upper()}{a}{i[0]} | {cla.upper()}{aa}{i[0]} || {cla.upper()}{aa}{i[1]} | {clave.upper()}{a}{i[1]} || ',datetime.now().strftime("%H:%M:%S  %d/%m/%Y"))

                                #Salgo si falta algun precio
                                if vendoA[0] == 10000 or comproB[0] == 10000 or vendoB[0] == 10000 or comproA[0] == 10000: break

                                #Hacer el calculo del rulo
                                cruzar(clave,cla,vendoA[0],comproB[0],vendoB[0],comproA[0])

                                #Cantidad de nominal a usar
                                if clave=='aap' or clave=='k' or clave=='amz': uso,res = nominal[1] , comA - nominal[1]
                                elif clave=='s30j' or clave=='s31g': uso,res = nominal[2] , comA - nominal[2]
                                else:  uso,res = nominal[0], comA - nominal[0]

                                #Evaluar el resultado 
                                if comA >= uso:

                                    #Cantidad LAST - uso puntas de bid/off    
                                    if vendoA[1] <= uso: break
                                    elif comproB[2] <= comB: break
                                    elif vendoB[1] <= comB:  break
                                    elif comproA[2] <= comA:  break
                                    #Cantidad en las PUNTAS: bid/off
                                    '''if vendoA[1] <= uso: break
                                    elif comproB[1] <= comB: break
                                    elif vendoB[1] <= comB: break
                                    elif comproA[1] <= comA: break'''

                                    #    ****    ENVIO DE OPERACIONES AL BROKER    ****
                                    '''if (clave=='s30j' or clave=='s31g') and (i[0]=='C' or i[0]=='D'): op.vender(('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[0]+' - '+u), uso, vendoA[0])
                                    else: op.vender(('MERV - XMEV - '+clave.upper()+a+i[0]+' - '+u),uso ,vendoA[0])
                                    ##########################################################
                                    if (cla=='s30j' or cla=='s31g') and (i[0]=='C' or i[0]=='D') : op.comprar(('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[0]+' - '+u), comB, comproB[0])
                                    else: op.comprar(('MERV - XMEV - '+cla.upper()+aa+i[0]+' - '+u),comB,comproB[0])
                                    ##########################################################
                                    if (cla=='s30j' or cla=='s31g') and (i[1]=='C' or i[1]=='D') : op.vender(('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[1]+' - '+u), comB, vendoB[0])
                                    else: op.vender(('MERV - XMEV - '+cla.upper()+aa+i[1]+' - '+u),comB,vendoB[0])
                                    ##########################################################
                                    if (clave=='s30j' or clave=='s31g') and (i[1]=='C' or i[1]=='D'): op.comprar(('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[1]+' - '+u), comA, comproA[0])
                                    else: op.comprar(('MERV - XMEV - '+clave.upper()+a+i[1]+' - '+u),comA,comproA[0])
                                    ##########################################################'''

                                    #Muestra candad de nominales ganados
                                    if clave+a in bonos: 
                                        for bonos_clave in bonos.keys():
                                            if bonos_clave == clave+a: bonos[bonos_clave] += res
                                    else: bonos[clave+a]=res
                                    if (clave + a) == 'al30' or (cla + aa) == 'al30': limite -= nominal[0]
                                    gana += res

                                    #Muestra resultado positivo
                                    if (clave=='s30j' or clave=='s31g') and (i[0]=='C' or i[0]=='D'): print('| -SI- |'+(clave[:1]+clave[3:]).upper()+a+i[0]+u.lower()+''+str(vendoA[0])+'|',end='')
                                    else: print('| SI |'+clave.upper()+a+i[0]+u.lower()+''+str(vendoA[0])+'|',end='')
                                    if (cla=='s30j' or cla=='s31g') and (i[0]=='C' or i[0]=='D'): print((cla[:1]+cla[3:]).upper()+aa+i[0]+u.lower()+''+str(comproB[0])+'| |',end='')
                                    else: print(cla.upper()+aa+i[0]+u.lower()+''+str(comproB[0])+'| |',end='') 
                                    if (cla=='s30j' or cla=='s31g') and (i[1]=='C' or i[1]=='D'): print((cla[:1]+cla[3:]).upper()+aa+i[1]+u.lower()+''+str(vendoB[0])+'|', end='')
                                    else: print(cla.upper()+aa+i[1]+u.lower()+''+str(vendoB[0])+'|', end='') 
                                    if (clave=='s30j' or clave=='s31g') and (i[1]=='C' or i[1]=='D'): print((clave[:1]+clave[3:]).upper()+a+i[1]+u.lower()+''+str(comproA[0])+
                                    '| |'+str(res)+'|'+str(limite)+'| |'+str(round(ccl,2))+'|'+str(round(mep,2))+'|'+ str(round(pes,2))+'| '+str(bonos))
                                    else: print(clave.upper()+a+i[1]+u.lower()+''+str(comproA[0])+'| |'+str(res)+'|'+str(limite)+'| |'+str(round(ccl,2))+'|'+str(round(mep,2))+'|'+ str(round(pes,2))+'| '+str(bonos))

                                    #Muestra tipo y catidad dinero
                                    resultado(e,clave,cla)
                                    continue

                                #Muestra resultado negativo
                                else:
                                    if (clave=='s30j' or clave=='s31g') and (i[0]=='C' or i[0]=='D'): print('|     |'+(clave[:1]+clave[3:]).upper()+a+i[0]+u.lower()+''+str(vendoA[0])+'|',end='')
                                    else: print('|   |'+clave.upper()+a+i[0]+u.lower()+''+str(vendoA[0])+'x'+str(uso)+'|',end='')
                                    if (cla=='s30j' or cla=='s31g') and (i[0]=='C' or i[0]=='D'): print((cla[:1]+cla[3:]).upper()+aa+i[0]+u.lower()+''+str(comproB[0])+'| |',end='')
                                    else: print(cla.upper()+aa+i[0]+u.lower()+''+str(comproB[0])+'| |',end='') 
                                    if (cla=='s30j' or cla=='s31g') and (i[1]=='C' or i[1]=='D'): print((cla[:1]+cla[3:]).upper()+aa+i[1]+u.lower()+''+str(vendoB[0])+'|', end='')
                                    else: print(cla.upper()+aa+i[1]+u.lower()+''+str(vendoB[0])+'|', end='') 
                                    if (clave=='s30j' or clave=='s31g') and (i[1]=='C' or i[1]=='D'): print((clave[:1]+clave[3:]).upper()+a+i[1]+u.lower()+''+str(comproA[0])+
                                    '| |'+str(res)+'|'+str(limite)+'| |'+str(round(ccl,2))+'|'+str(round(mep,2))+'|'+ str(round(pes,2))+'| '+str(bonos))
                                    else: print(clave.upper()+a+i[1]+u.lower()+''+str(comproA[0])+'| |'+str(res)+'|'+str(limite)+'| |'+str(round(ccl,2))+'|'+str(round(mep,2))+'|'+ str(round(pes,2))+'| '+str(bonos))
                                
                                    break

                                
