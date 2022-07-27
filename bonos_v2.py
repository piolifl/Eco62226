from Consultar import Consultar
from Operar import Operar
from datetime import datetime
import math
import time

hora = time.strftime("%H:%M:%S")
fecha_hora = datetime.now().strftime("%H:%M:%S  %d/%m/%Y")

while True:
    if hora < '11:00:00':
        print('Esperando la apertura ...', fecha_hora),time.sleep(10)
        continue
    else: break

pr = Consultar()
op = Operar()

costos = 0.0026
limite = 99999
gana = 0
ccl = 0
mep = 0
pes = 0
bonos = {}
vuelta = 1

tipo = {'al':['30'],'gd':['30','35'], 
#'s29l':['2'], #'s31g':['2'],'s29l':['2'],#'s31o':['2'],
#'aap':['L'], #'k':['O'], #'amz':['N'],
#'al':['30','29','35','41'],'ae':['38'],'gd':['30','29','35','38','41','46']
}

if hora < '16:29:55': plazo = ['CI','48hs','24hs']
else: plazo = ['48hs','24hs']

moneda = {
'ccl|mep':['C','D'],
#'ccl|pes':['C',''],
'#mep|ccl':['D','C'],
#'mep|pes':['D','']
}
nominal = [1000,2,1500]

def cruzar(tA,tB,vendo1,compro2,vendo2,compro1):
    global comA,comB,venA,venB
    if tA=='aap' or tA=='k' or tA=='amz': venA = round(vendo1 * nominal[1] * (1-costos),2)
    elif tA=='s29l' or tA=='s31g': venA = round((vendo1/100) * nominal[2] * (1-costos),2)
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
    #if hora > '16:29:55': plazo = ['48hs','24hs']
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
                                if (clave=='s29l' or clave=='s31g') and (i[0]=='C' or i[0]=='D'): vendoA = pr.precioLA('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[0]+' - '+u)
                                else: vendoA = pr.precioLA( 'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' +u)
                                if (cla=='s29l' or cla=='s31g') and (i[0]=='C' or i[0]=='D'): comproB= pr.precioLA('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[0]+' - '+u)
                                else: comproB= pr.precioLA( 'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u)
                                if (cla=='s29l' or cla=='s31g') and (i[1]=='C' or i[1]=='D'): vendoB = pr.precioLA('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[1]+' - '+u)
                                else: vendoB = pr.precioLA( 'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u)
                                if (clave=='s29l' or clave=='s31g') and (i[1]=='C' or i[1]=='D'): comproA= pr.precioLA('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[1]+' - '+u)
                                else: comproA= pr.precioLA( 'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' +u)

                                #Consulto precios PUNTAS 
                                '''if (clave=='s29l' or clave=='s31g') and (i[0]=='C' or i[0]=='D'): vendoA = pr.precioBI('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[0]+' - '+u)
                                else: vendoA = pr.precioBI( 'MERV - XMEV - ' + clave.upper() + a + i[0] + ' - ' +u)
                                if (cla=='s29l' or cla=='s31g') and (i[0]=='C' or i[0]=='D'): comproB= pr.precioOF('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[0]+' - '+u)
                                else: comproB= pr.precioOF( 'MERV - XMEV - ' + cla.upper() + aa + i[0] + ' - ' + u)
                                if (cla=='s29l' or cla=='s31g') and (i[1]=='C' or i[1]=='D'): vendoB = pr.precioBI('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[1]+' - '+u)
                                else: vendoB = pr.precioBI( 'MERV - XMEV - ' + cla.upper() + aa + i[1] + ' - ' + u)
                                if (clave=='s29l' or clave=='s31g') and (i[1]=='C' or i[1]=='D'): comproA= pr.precioOF('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[1]+' - '+u)
                                else: comproA= pr.precioOF( 'MERV - XMEV - ' + clave.upper() + a + i[1] + ' - ' +u)'''
                                
                                #Salgo si falta algun precio
                                if vendoA[0] == 10000 or comproB[0] == 10000 or vendoB[0] == 10000 or comproA[0] == 10000:
                                    print(f'Buscando... {u} | {clave.upper()}{a}{i[0]} | {cla.upper()}{aa}{i[0]} || {cla.upper()}{aa}{i[1]} | {clave.upper()}{a}{i[1]} || ',datetime.now().strftime("%H:%M:%S  %d/%m/%Y"))
                                    break

                                #Hacer el calculo del rulo
                                cruzar(clave,cla,vendoA[0],comproB[0],vendoB[0],comproA[0])

                                #Cantidad de nominal a usar
                                if clave=='aap' or clave=='k' or clave=='amz': uso,res = nominal[1] , comA - nominal[1]
                                elif clave=='s29l' or clave=='s31g': uso,res = nominal[2] , comA - nominal[2]
                                else:  uso,res = nominal[0], comA - nominal[0]

                                #Evaluar el resultado 
                                if comA >= uso:

                                    #Cantidad LAST - uso puntas de bid/off   
                                    if vendoA[1] <= uso: break
                                    elif comproB[2] <= comB: break
                                    elif vendoB[1] <= comB: break
                                    elif comproA[2] <= comA: break
                                    #Cantidad en las PUNTAS: bid/off
                                    '''if vendoA[1] <= uso: break
                                    elif comproB[1] <= comB: break
                                    elif vendoB[1] <= comB: break
                                    elif comproA[1] <= comA: break'''

                                    #    ****    ENVIO DE OPERACIONES AL BROKER    ****
                                    '''if (clave=='s29l' or clave=='s31g') and (i[0]=='C' or i[0]=='D'): op.vender(('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[0]+' - '+u), uso, vendoA[0])
                                    else: op.vender(('MERV - XMEV - '+clave.upper()+a+i[0]+' - '+u),uso ,vendoA[0])
                                    ##########################################################
                                    if (cla=='s29l' or cla=='s31g') and (i[0]=='C' or i[0]=='D'):op.comprar(('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[0]+' - '+u), comB, comproB[0])
                                    else:op.comprar(('MERV - XMEV - '+cla.upper()+aa+i[0]+' - '+u),comB,comproB[0])
                                    ##########################################################
                                    if (cla=='s29l' or cla=='s31g') and (i[1]=='C' or i[1]=='D'): op.vender(('MERV - XMEV - '+(cla[:1]+cla[3:]).upper()+aa+i[1]+' - '+u), comB, vendoB[0])
                                    else: op.vender(('MERV - XMEV - '+cla.upper()+aa+i[1]+' - '+u),comB,vendoB[0])
                                    ##########################################################
                                    if (clave=='s29l' or clave=='s31g') and (i[1]=='C' or i[1]=='D'): op.comprar(('MERV - XMEV - '+(clave[:1]+clave[3:]).upper()+a+i[1]+' - '+u), comA, comproA[0])
                                    else: op.comprar(('MERV - XMEV - '+clave.upper()+a+i[1]+' - '+u),comA,comproA[0])
                                    ##########################################################'''

                                    #Muestra candad de nominales ganados
                                    if clave+a in bonos: 
                                        for bonos_clave in bonos.keys():
                                            if bonos_clave == clave+a: bonos[bonos_clave] += res
                                    else: bonos[clave+a]=res
                                    gana += res

                                    #Muestra resultado positivo
                                    if (clave=='s29l' or clave=='s31g') and (i[0]=='C' or i[0]=='D'): print('| SI |'+u.lower()+'|'+(clave[:1]+clave[3:]).upper()+a+i[0]+''+str(vendoA[0])+' ',end='')
                                    else: print('| SI |'+u.lower()+'|'+clave.upper()+a+i[0]+''+str(vendoA[0])+' ',end='')
                                    if (cla=='s29l' or cla=='s31g') and (i[0]=='C' or i[0]=='D'): print((cla[:1]+cla[3:]).upper()+aa+i[0]+''+str(comproB[0])+'| |',end='')
                                    else: print(cla.upper()+aa+i[0]+''+str(comproB[0])+'| |',end='') 
                                    if (cla=='s29l' or cla=='s31g') and (i[1]=='C' or i[1]=='D'): print((cla[:1]+cla[3:]).upper()+aa+i[1]+''+str(vendoB[0])+' ', end='')
                                    else: print(cla.upper()+aa+i[1]+''+str(vendoB[0])+' ', end='') 
                                    if (clave=='s29l' or clave=='s31g') and (i[1]=='C' or i[1]=='D'): print((clave[:1]+clave[3:]).upper()+a+i[1]+''+str(comproA[0])+
                                    '| |'+str(res)+'|'+str(limite)+'| |'+str(round(ccl,2))+'|'+str(round(mep,2))+'|'+ str(round(pes,2))+'| '+str(bonos))
                                    else: print(clave.upper()+a+i[1]+''+str(comproA[0])+'| |'+str(round(res))+'|'+str(limite)+'| |'+str(round(ccl,2))+'|'+str(round(mep,2))+'|'+ str(round(pes,2))+'| '+str(bonos))

                                    #Muestra tipo y catidad dinero
                                    resultado(e,clave,cla)

                                    #Reduce disponible de al30
                                    if (clave + a) == 'al30' or (cla + aa) == 'al30': limite -= nominal[0]

                                    #Control de vueltas en mismo papel
                                    vuelta += 1
                                    if vuelta > 5: 
                                        vuelta = 1
                                        if hora > '16:29:00': plazo = ['48hs','24hs']
                                        if hora > '16:59:55': exit()
                                        break
                                    else: 
                                        if hora > '16:29:00': plazo = ['48hs','24hs']
                                        if hora > '16:59:55': exit()
                                        continue
                                    
                                #Muestra resultado negativo
                                else:
                                    if (clave=='s29l' or clave=='s31g') and (i[0]=='C' or i[0]=='D'): print('|    |'+u.lower()+'|'+(clave[:1]+clave[3:]).upper()+a+i[0]+''+str(vendoA[0])+' ',end='')
                                    else: print('|    |'+u.lower()+'|'+clave.upper()+a+i[0]+''+str(vendoA[0])+' ',end='')
                                    if (cla=='s29l' or cla=='s31g') and (i[0]=='C' or i[0]=='D'): print((cla[:1]+cla[3:]).upper()+aa+i[0]+''+str(comproB[0])+'| |',end='')
                                    else: print(cla.upper()+aa+i[0]+''+str(comproB[0])+'| |',end='') 
                                    if (cla=='s29l' or cla=='s31g') and (i[1]=='C' or i[1]=='D'): print((cla[:1]+cla[3:]).upper()+aa+i[1]+''+str(vendoB[0])+' ', end='')
                                    else: print(cla.upper()+aa+i[1]+''+str(vendoB[0])+' ', end='') 
                                    if (clave=='s29l' or clave=='s31g') and (i[1]=='C' or i[1]=='D'): print((clave[:1]+clave[3:]).upper()+a+i[1]+''+str(comproA[0])+
                                    '| |'+str(res)+'|'+str(limite)+'| |'+str(round(ccl,2))+'|'+str(round(mep,2))+'|'+ str(round(pes,2))+'| '+str(bonos))
                                    else: print(clave.upper()+a+i[1]+''+str(comproA[0])+'| |'+str(round(res))+'|'+str(limite)+'| |'+str(round(ccl,2))+'|'+str(round(mep,2))+'|'+ str(round(pes,2))+'| '+str(bonos))
                                    if hora > '16:59:55': exit()
                                    break

                                
