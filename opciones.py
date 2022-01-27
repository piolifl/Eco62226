from Consultar import Consultar
from Operar import Operar
import math
import time

pr = Consultar()
op = Operar()


ratio = {'1':['180',1,27,'200',2,13.59]}

while True:
    if ratio['1'][0] == '0': break
    for item, valor in ratio.items():
        if valor[0] == '0': continue
        vendo  = pr.precioBI('MERV - XMEV - ' + 'GFGC' + valor[0] + '.FE' + ' - ' + '24hs')
        compro = pr.precioBI('MERV - XMEV - ' + 'GFGC' + valor[3] + '.FE' + ' - ' + '24hs')
        if vendo == 1000 or compro == 1000:
            print(time.strftime("%H:%M:%S"),f'SIN PRECIOS | {valor[0]} a {vendo} x {valor[1]} contra {valor[3]} a {compro} x {valor[4]}'),time.sleep(5)
            continue
        ratioE = round(valor[2] / valor[5],3) 
        ratioA = round(vendo / compro,2)
        if  ratioA > ratioE * (1 + 0.25):

            pr.logRulos(time.strftime("%H:%M:%S") + 'CERRADO: ' + valor[0] + 'a' + vendo + 'x' + valor[1] + 'contra' + valor[3] + 'a' + compro + 'x' + valor[4] + '')
            print(time.strftime("%H:%M:%S"),f'CERRADO | {valor[0]} a {vendo} x {valor[1]} contra {valor[3]} a {compro} x {valor[4]}')

            #op.vender   (('MERV - XMEV - ' + 'GFGC' + valor[0] + '.FE' + ' - ' + '24HS'),valor[1],vendo)
            #op.comprar  (('MERV - XMEV - ' + 'GFGC' + valor[3] + '.FE' + ' - ' + '24HS'),valor[4],compro)

            ratio[item][0] = '0'

        else: print(time.strftime("%H:%M:%S"),f'BUSCANDO | {valor[0]} a {vendo} x {valor[1]} contra {valor[3]} a {compro} x {valor[4]}')