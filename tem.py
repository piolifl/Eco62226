from matplotlib import ticker
from numpy import append
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
uso = 200

tipo = {'al':['29','30','35','41'],    'ae':['38'],     'gd':['29','30','35','38','41','46']
}
moneda = {'ccl-mep':['C','D'],  'mep-ccl':['D','C'], 'mep-pes':['D',''] , 'ccl-pes':['C','']
}
plazo = ['CI','48hs','24hs']

par = []

for clave, valor in tipo.items():
    for a in valor:
        for e,i in moneda.items():
            for o in i:
                for u in plazo:
                    par.append('MERV - XMEV - ' + clave.upper() + a + o + ' - ' + u)

                    
                    #print(f'Ticker: MERV - XMEV - {clave.upper()}{a}{o} - {u}')
                    #pr_vendoA =   pr.precioBI( 'MERV - XMEV - ' + clave.upper() + a + o + ' - ' + u )
print(par)


