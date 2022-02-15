'''from matplotlib import ticker
from numpy import append
from Consultar import Consultar
from Operar import Operar
from datetime import datetime
import math
import time

pr = Consultar()
op = Operar()'''

costos = 0.0026
limite = 1000
gana = 0
ccl = 0
mep = 0
peso = 0
uso = 200
al = []
ae = []
gd = []
let = []
ced = []


tipo = {'al':['30','29','35','41'], 'ae':['38'], 'gd':['30','29','35','38','41','46'], 'let':[], 'ced':[]}
mone = ['C','D','']
plazo = ['CI','48hs','24hs']

for clave, valor in tipo.items():
    for a in valor:
        for i in mone:
            for u in plazo:
                if clave == 'al':
                    al.append('MERV - XMEV - ' + clave.upper() + a + i + ' - ' + u)
                elif clave == 'ae':
                    ae.append('MERV - XMEV - ' + clave.upper() + a + i + ' - ' + u)
                elif clave == 'gd':
                    gd.append('MERV - XMEV - ' + clave.upper() + a + i + ' - ' + u)
                elif clave == 'let':
                    let.append('MERV - XMEV - ' + clave.upper() + a + i + ' - ' + u)
                elif clave == 'ced':
                    ced.append('MERV - XMEV - ' + clave.upper() + a + i + ' - ' + u)
                #print(f'Ticker: MERV - XMEV - {clave.upper()}{a}{o} - {u}')
                #pr_vendoA =   pr.precioBI( 'MERV - XMEV - ' + clave.upper() + a + o + ' - ' + u )





