from Consultar import Consultar
from Operar import Operar
import math
import time

pr = Consultar()
op = Operar()

costo = 0.005

ratio = {
    '1':['GFG','V','200','.AB',1,9.1,    '190',2,   5.26,     0.15 ],
    '2':['GFG','C','0','.AB',1,19.23,  '220',2,   10.25,    0.15 ],
    '3':['GFG','C','200','.AB',1,20.3,   '220',2,   11.15,    0.15 ],
    '4':['GFG','C','210','.AB',1,15.95,  '230',2,   8.61,     0.15 ]
}

while True:
    if time.strftime("%H:%M:%S") < '11:00:00':
        print(time.strftime("%H:%M:%S"),'Esperando la apertura a las 11hs ... '),time.sleep(5)
        continue
    if time.strftime("%H:%M:%S") > '16:59:50':
        print(f'FIN 17hs CERRADO |')
        break
    for item, valor in ratio.items():
        if valor[2] == '0': continue
        vendo  = pr.precioBI('MERV - XMEV - ' + valor[0] + valor[1] + valor[2] + valor[3] +' - ' + '24hs')
        compro = pr.precioOF('MERV - XMEV - ' + valor[0] + valor[1] + valor[6] + valor[3] +' - ' + '24hs')
        if vendo == 1000 or compro == 1000: continue
        ratioE = round(valor[5] / valor[8],3) 
        ratioA = round(vendo / compro,2)
        res = round(((((valor[7] * valor[8])*(1-costo)) - ((compro * valor[7]) * (1+costo) ) ) - (((valor[4] * valor[5])*(1+costo)) - ((vendo * valor[4])*(1-costo)))) *100,2)
        dif = round((ratioA/ratioE -1)*100,2)

        if  ratioA > (ratioE * (1 + valor[9])):

            if   pr.bidsBI(  'MERV - XMEV - ' + valor[0] + valor[1] + valor[2] + valor[3] +' - ' + '24hs') == 0: continue
            elif pr.offersOF('MERV - XMEV - ' + valor[0] + valor[1] + valor[6] + valor[3] +' - ' + '24hs') == 0: continue

            #op.vender   (('MERV - XMEV - ' + valor[0] + valor[1] + valor[2] + valor[3] +' - ' + '24hs'),  valor[4],   round(vendo,3))
            #op.comprar  (('MERV - XMEV - ' + valor[0] + valor[1] + valor[6] + valor[3] +' - ' + '24hs'),  valor[7],   round(compro,3))

            pr.logRatios('CERRADO: ' + str(valor[0]) + ' | '  + str(valor[0]) + ' | ' + ' Resultado ' + str(res)   )

            print(time.strftime("%H:%M:%S"),f'| CERRADO | {valor[0]}{valor[1]}{valor[2]}{valor[3]}: {vendo} | {valor[0]}{valor[1]}{valor[6]}{valor[3]}: {compro} || resultado: {res}')

            ratio[item][2] = '0'

        else: print(time.strftime("%H:%M:%S"),f'| {item} | {valor[0]}{valor[1]}{valor[2]}{valor[3]}: {vendo} | {valor[0]}{valor[1]}{valor[6]}{valor[3]}: {compro} || resultado: {res}')
        time.sleep(2)
            


        