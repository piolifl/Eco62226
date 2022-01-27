from cgitb import reset
from Consultar import Consultar
from Operar import Operar
import math
import time

pr = Consultar()
op = Operar()


ratio = {'1':['180',1,27,'200',2,13.59], '2':['190',1,20,'220',2,10.59]}

while True:
    if ratio['1'][0] == '0': break
    for item, valor in ratio.items():
        if valor[0] == '0': continue
        vendo  = pr.precioBI('MERV - XMEV - ' + 'GFGC' + valor[0] + '.FE' + ' - ' + '24hs')
        compro = pr.precioOF('MERV - XMEV - ' + 'GFGC' + valor[3] + '.FE' + ' - ' + '24hs')
        if vendo == 1000 or compro == 1000:
            print(time.strftime("%H:%M:%S"),f' | SIN PRECIOS | {valor[0]} a {vendo} x {valor[1]} contra {valor[3]} a {compro} x {valor[4]} '),time.sleep(5)
            continue
        ratioE = round(valor[2] / valor[5],3) 
        ratioA = round(vendo / compro,2)
        res = round(    ((valor[2] * valor[1]) - (vendo * valor[1])) - ((valor[4] * valor[5]) - (compro * valor[4]))    ,2)
        if  ratioA > ratioE * (1 + 0.25):

            pr.logRatios('CERRADO: ' + str(valor[0]) + ' a ' + str(vendo) + ' x ' + str(valor[1]) + ' contra ' + str(valor[3]) + ' a ' + str(compro) + ' x ' + str(valor[4]) + ' resultado ' + str(res))
            print(time.strftime("%H:%M:%S"),f' | CERRADO | {valor[0]} a {vendo} x {valor[1]} contra {valor[3]} a {compro} x {valor[4]} resultado {res}')

            #op.vender   (('MERV - XMEV - ' + 'GFGC' + valor[0] + '.FE' + ' - ' + '24HS'),valor[1],vendo)
            #op.comprar  (('MERV - XMEV - ' + 'GFGC' + valor[3] + '.FE' + ' - ' + '24HS'),valor[4],compro)

            ratio[item][0] = '0'

        else: print(time.strftime("%H:%M:%S"),f' | BUSCANDO | {valor[0]} a {vendo} x {valor[1]} contra {valor[3]} a {compro} x {valor[4]} resultado {res}')