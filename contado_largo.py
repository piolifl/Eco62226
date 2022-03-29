from Consultar import Consultar
from Operar import Operar
from datetime import datetime
import math
import time

pr = Consultar()
op = Operar()

costos = 0.0052
ganancia = 0.5

tipo = {'AL':['30'],'GD':['30'],'AE':['38'],'GGA':['L'],'PAM':['P'],'AL':['30','29','35','41'],'AE':['38'],'GD':['30','29','35','38','41','46'],#'AAP':['L'],'K':['O']
}
moneda = {'1':[''#,'D'#,'C'
]}
plazo = ['CI','48hs','24hs']

nominal = 25
limite = 25

def activar(buy,cantidad,com_precio,sell,ven_precio):
    #op.comprar(buy,cantidad,com_precio)
    print(buy,cantidad,com_precio)
    #op.vender(sell,cantidad,ven_precio)
    print(sell,cantidad,ven_precio)

while True:
    for clave,valor in tipo.items():
        for e in valor:
            for cla,val in moneda.items():
                for i in val:
                    taza = pr.precioLA('MERV - XMEV - PESOS - 1D')
                    dias = 1
                    if taza == 1000:
                        taza = pr.precioLA('MERV - XMEV - PESOS - 2D')
                        dias = 2
                        if taza == 1000:
                            taza = pr.precioLA('MERV - XMEV - PESOS - 3D')
                            dias = 3
                            if taza == 1000:
                                taza = pr.precioLA('MERV - XMEV - PESOS - 4D')
                                dias = 4
                                if taza == 1000:
                                    taza = pr.precioLA('MERV - XMEV - PESOS - 5D')
                                    dias = 5
                    tna = round(taza/100/365,5)

                    cont_of = pr.precioOF('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[0])
                    larg_bi = pr.precioBI('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[1])
                    medi_of = pr.precioOF('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[2])
                    medi_bi = pr.precioBI('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[2])
                
                    libreR = round(cont_of/100*nominal*tna*dias,2)

                    if cont_of == 1000 or larg_bi == 1000: continue
                    else:
                        if (larg_bi/100*nominal) > (cont_of/100*nominal): ci_48 = round((((larg_bi/100*nominal)*(1-costos)) - (cont_of/100*nominal)),2)
                        else: ci_48 = round(((larg_bi/100*nominal) - (cont_of/100*nominal))*(1-costos),2)
                    if medi_bi == 1000: continue
                    else:  
                        if (medi_bi/100*nominal) > (cont_of/100*nominal): ci_24 = round((((medi_bi/100*nominal)*(1-costos)) - (cont_of/100*nominal)),2)
                        else: ci_24 = round(((medi_bi/100*nominal) - (cont_of/100*nominal))*(1-costos),2)
                    if medi_of == 1000: continue
                    else:
                        if (larg_bi/100*nominal) > (medi_of/100*nominal): ve_cu = round((((larg_bi/100*nominal)*(1-costos)) - (medi_of/100*nominal)),2)
                        else: ve_cu = round(((larg_bi/100*nominal) - (medi_of/100*nominal))*(1-costos),2)
                    if ci_48 > (libreR * (1 + ganancia)):
                        activar( ('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[0]), nominal, cont_of , ('MERV - XMEV - ' + clave + e + i +  ' - ' + plazo[1]) , larg_bi   )
                        print(f'SI ci {clave+e} contra 48 {clave+e} | ',ci_48)
                        limite -= nominal
                        continue
                    elif ci_24 > (libreR * (1 + ganancia)):
                        activar( ('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[0]), nominal, cont_of , ('MERV - XMEV - ' + clave + e + i +  ' - ' + plazo[2]) , medi_bi   )
                        print(f'SI ci {clave+e} contra 24 {clave+e} | ',ci_24)    
                        limite -= nominal
                        continue
                    elif ve_cu > (libreR * (1 + ganancia)):
                        activar( ('MERV - XMEV - ' + clave + e + i + ' - ' + plazo[2]), nominal, medi_of , ('MERV - XMEV - ' + clave + e + i +  ' - ' + plazo[1]) , larg_bi   )
                        print(f'SI 24 {clave+e} contra 48 {clave+e} | ',ve_cu)
                        limite -= nominal
                        continue
                        
                    else: 
                        print('| no | '+clave+ e+i+'-'+plazo[0] + ' | '+ str(round(cont_of/100,2) * nominal) + ' | ' + clave + e + i + '-' + plazo[1] + ' | '+ str(round(larg_bi/100,2) * nominal) + ' = ' + str(ci_48))
                        print('| no | '+clave+ e+i+'-'+plazo[0] + ' | '+ str(round(cont_of/100,2) * nominal) + ' | ' + clave + e + i + '-' + plazo[2] + ' | '+ str(round(medi_bi/100,2) * nominal) + ' = ' + str(ci_24))
                        print('| no | '+clave+ e+i+'-'+plazo[2] + ' | '+ str(round(medi_of/100,2) * nominal) + ' | ' + clave + e + i + '-' + plazo[1] + ' | '+ str(round(larg_bi/100,2) * nominal) + ' = ' + str(ve_cu))
                        



