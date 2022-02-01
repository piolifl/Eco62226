from Consultar import Consultar
from Operar import Operar
import math
import time

pr = Consultar()
op = Operar()

costo = 0.005

ratio = {
    '1':['GFG','C','180','.FE',1,27, '200',2,13.59 ],
    '2':['GFG','C','250','.AB',10,5.7, '270',15,3.89 ],
    '3':['GFG','V','210','.AB',10,8, '195',15,5.5 ]
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
        res = round(    (((valor[4] * valor[5])*(1+costo)) - ((vendo * valor[4])*(1-costo)))    -   (   ((valor[7] * valor[8])*(1-costo)) - ((compro * valor[7]) * (1+costo) ) )   ,2)

        if  ratioA > ratioE * (1 + 0.45):

            if   pr.bidsBI(  'MERV - XMEV - ' + valor[0] + valor[1] + valor[2] + valor[3] +' - ' + '24hs') == 0: continue
            elif pr.offersOF('MERV - XMEV - ' + valor[0] + valor[1] + valor[6] + valor[3] +' - ' + '24hs') == 0: continue

            #op.vender   (('MERV - XMEV - ' + valor[0] + valor[1] + valor[2] + valor[3] +' - ' + '24hs'),  valor[4],   vendo)
            #op.comprar  (('MERV - XMEV - ' + valor[0] + valor[1] + valor[6] + valor[3] +' - ' + '24hs'),  valor[7],   compro)

            pr.logRatios('CERRADO: ' + str(valor[0],valor[1],valor[2],valor[3]) + ' | '  + str(valor[0],valor[1],valor[6],valor[3]) + ' | ' + ' Resultado ' + str(res)   )

            print(time.strftime("%H:%M:%S"),f' | CERRADO | {valor[0]}{valor[1]}{valor[2]}{valor[3]} a {vendo} | {valor[0]}{valor[1]}{valor[6]}{valor[3]} a {compro} |  resultado {res}')

            ratio[item][2] = '0'

        else: print(time.strftime("%H:%M:%S"),f' | BUSCANDO | {valor[0]}{valor[1]}{valor[2]}{valor[3]} a {vendo} | {valor[0]}{valor[1]}{valor[6]}{valor[3]} a {compro} | resultado {res}')
        time.sleep(5)

        