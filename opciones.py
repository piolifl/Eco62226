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

costo = 0.0052

ratio = {
    '1':['GFG','C','185','.AG',1,10.88,  '195',2,   6.5,  0.15 ],
    '2':['GFG','C','0','.AG',1,24.93, '220',2,   14,    0.15 ],
    '3':['GFG','C','0','.AG',1,20.3,   '220',2,   11.15,  0.15 ]
}

while True:
    if time.strftime("%H:%M:%S") > '17:59:50':
        print(f'FIN 17hs MERCADO CERRADO |', datetime.now().strftime("%H:%M:%S  %d/%m/%Y"))
        break
    for item, valor in ratio.items():
        if valor[2] == '0': continue
        vendo = pr.precioBI('MERV - XMEV - '+valor[0]+valor[1]+valor[2]+valor[3]+' - '+'24hs')
        compro= pr.precioOF('MERV - XMEV - '+valor[0]+valor[1]+valor[6]+valor[3]+' - '+'24hs')
        if vendo[0] == 10000 or compro[0] == 10000: continue

        ratioE = round(valor[5] / valor[8],3) 
        ratioA = round(vendo[0] / compro[0],3)
        ratioO = round(ratioE * (1+ valor[9]),3)

        res = round(((((valor[7] * valor[8])*(1-costo)) - ((compro[0] * valor[7]) * (1+costo) ) ) - (((valor[4] * valor[5])*(1+costo)) - ((vendo[0] * valor[4])*(1-costo)))) *100,2)
        dif = round((ratioA/ratioE -1)*100,2)

        if  ratioA > ratioO:
            if vendo[1] == 0 or compro[1] == 0: continue

            '''op.comprar  (('MERV - XMEV - ' + valor[0] + valor[1] + valor[6] + valor[3] +' - ' + '24hs'),  valor[7],   round(compro[0],3))
            op.vender   (('MERV - XMEV - ' + valor[0] + valor[1] + valor[2] + valor[3] +' - ' + '24hs'),  valor[4],   round(vendo[0],3))'''

            print(time.strftime("%H:%M:%S"),f'| CERRADA | {valor[0]}{valor[1]}{valor[2]}{valor[3]}: {vendo[0]} | {valor[0]}{valor[1]}{valor[6]}{valor[3]}: {compro[0]} || re: {res} raE: {ratioE} raA: {ratioA} raO: {ratioO} dif: {dif}')

            ratio[item][2] = '0'

        else: print(time.strftime("%H:%M:%S"),f'| {item} | {valor[0]}{valor[1]}{valor[2]}{valor[3]}: {vendo[0]} | {valor[0]}{valor[1]}{valor[6]}{valor[3]}: {compro[0]} || re: {res} raE: {ratioE} raA: {ratioA} raO: {ratioO} dif: {dif}')
        time.sleep(2)
            




        