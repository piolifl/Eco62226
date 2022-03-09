from Consultar import Consultar
from Operar import Operar
from datetime import datetime
import math
import time

pr = Consultar()
op = Operar()

costos = 0.0026

moneda = {
    'ccl-mep':['C','D'],  'mep-ccl':['D','C'],'mep-pes':['D',''] , 'ccl-pes':['C','']
}

plazo = {'1': ['CI','48hs','24hs']}

ticker = {'1':['AL30'],'2':['gd30']}
#tipo = {'AL':['30','29'],'AE':['38']}

while True:
    if time.strftime("%H:%M:%S") < '11:00:00':
        print('Esperando la apertura ...', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),time.sleep(10)
        continue
    if time.strftime("%H:%M:%S") > '16:59:50':
        print(f'FIN 17hs CERRADO | ')
        break
    if time.strftime("%H:%M:%S") > '15:59:45': plazo = ['48hs','24hs']

    for clave, valor in ticker.items():
        for e,i in moneda.items():
            for a,u in plazo.items():
                while True:
                    comproCI =   pr.precioBI( 'MERV - XMEV - ' + valor[0].upper() + i[0] + ' - ' + u[0])/100
                    vendo48 =    pr.precioOF( 'MERV - XMEV - ' + valor[0].upper() + i[0] + ' - ' + u[1] )/100
                    vendo24 =    pr.precioOF( 'MERV - XMEV - ' + valor[0].upper() + i[0] + ' - ' + u[2] )/100
                    pesos1D = round(pr.precioLA( 'MERV - XMEV - PESOS - 1D')/365/30,4)
                    if comproCI == 1000 or vendo48 == 1000 or vendo24 == 1000: break

                    if comproCI  < vendo48 * (pesos1D * 2) * costos:
                        contra48 = round((vendo48 * 10) - (comproCI * 10),4)
                        print(f'Exito, gana en 48 : {contra48}')
                    elif comproCI  < vendo24 * (pesos1D * 2) * costos:
                        contra24 = round((vendo24 * 10) - (comproCI * 10),2)
                        print(f'Exito, gana en 24 : {contra24}')
                    else:
                        print('MERV - XMEV - ' + valor[0].upper() + str(i[0]) + ' - ' + str(u[0]) + ' | ' + str(comproCI))
                        print('MERV - XMEV - ' + valor[0].upper() + str(i[0]) + ' - ' + str(u[2]) + ' | ' + str(vendo24))
                        print('MERV - XMEV - ' + valor[0].upper() + str(i[0]) + ' - ' + str(u[1]) + ' | ' + str(vendo48))
                        print(f'taza: {pesos1D}')
                        contra48 = round((vendo48 * 10) - (comproCI * 10),2)
                        print(f'Resultado opracion contra48 | {contra48}')
                        contra24 = round((vendo24 * 10) - (comproCI * 10),2)
                        print(f'Resultado opracion contra24 | {contra24}')
                        time.sleep(5)
                        break





