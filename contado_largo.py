from Consultar import Consultar
from Operar import Operar
from datetime import datetime
import math
import time

pr = Consultar()
op = Operar()

costos = 0.0052
ganancia = 0.5

tipo = {'AL':['30','29'],'GD':['30'],'AE':['38'],'GGA':['L']#'AL':['30','29','35','41'],'ae':['38'],'gd':['30','29','35','38','41','46'],'aap':['L'],'k':['O']
}
moneda = {'1':[''#,'D'#,'C'
]}
plazo = ['CI','48hs','24hs']

nominal = 25
limite = 25

def activar(com_ticker,cantidad,com_precio,ven_ticker,ven_precio):
    #op.comprar(com_ticker,cantidad,com_precio)
    print(com_ticker,cantidad,com_precio)
    #op.vender(ven_ticker,cantidad,ven_precio)
    print(ven_ticker,cantidad,ven_precio)

while True:
    for clave,valor in tipo.items():
        for e in valor:
            for cla,val in moneda.items():
                for i in val:
                    taza = pr.precioOF('MERV - XMEV - PESOS - 1D')
                    dias = 1
                    if taza == 1000:
                        taza = pr.precioOF('MERV - XMEV - PESOS - 3D')
                        dias = 3
                        if taza == 1000:
                            taza = pr.precioOF('MERV - XMEV - PESOS - 5D')
                            dias = 5
                    tna = round(taza/100/365,5)

                    cont_of = pr.precioOF('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[0])
                    larg_of = pr.precioLA('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[1])
                    medi_of = pr.precioOF('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[2])
                    medi_bi = pr.precioBI('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[2])
                    if cont_of == 1000 or larg_of == 1000 or medi_of == 1000 or medi_bi == 1000: continue

                    libreR = round(cont_of/100*nominal*tna*dias,2)

                    ci_48 = round(((larg_of/100*nominal) - (cont_of/100*nominal))*(1-costos),2)
                    ci_24 = round(((medi_of/100*nominal) - (cont_of/100*nominal))*(1-costos),2)
                    ven_cua = round(((larg_of/100*nominal) - (medi_of/100*nominal))*(1-costos),2)

                    if ci_48 > (libreR * (1 + ganancia)):
                        activar( ('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[0]), nominal, cont_of , ('MERV - XMEV - ' + clave + e + i +  ' - ' + plazo[1]) , larg_of   )
                        print('SI ci contra 48')
                        limite -= nominal
                    elif ci_24 > (libreR * (1 + ganancia)):
                        activar( ('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[0]), nominal, cont_of , ('MERV - XMEV - ' + clave + e + i +  ' - ' + plazo[2]) , larg_of   )
                        print('SI ci contra 24')
                        limite -= nominal
                    elif ven_cua > (libreR * (1 + ganancia)):
                        activar( ('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[2]), nominal, cont_of , ('MERV - XMEV - ' + clave + e + i +  ' - ' + plazo[1]) , larg_of   )
                        print('SI 24 contra 48')
                        limite -= nominal
                        
                    else: 
                        print('nada')
                        print('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[0] + ' | '+ str(cont_of))
                        print('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[1] + ' | '+ str(larg_of))
                        print('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[2] + ' | '+ str(medi_of))
                        print('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[2] + ' | '+ str(medi_bi))


