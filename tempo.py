
bonos = {}

while True:
    print(bonos)
    a=input('continua ...')
    if a != '':
        print(bonos)
        break
    clave = input('bono: ')
    valor = input('valor: ')
    #bonos[clave]= valor
    if 'al30' in bonos:
        print('si esta ')
        bonos[clave.upper()]= valor
    else: bonos[clave]= valor 
    print(bonos)


    









