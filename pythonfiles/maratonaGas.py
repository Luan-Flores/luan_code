
while True:
    combust=input('Qual? (A)Alcool (G)Gasolina').lower()
    litros=float(input('Quantos litros? '))
    if combust=='a':
        if litros<=20:
            calc_alcool=(1.9*litros)
            descon=(3/100)*(calc_alcool)
            print(f'Valor total: {calc_alcool-descon}')
            break
        elif litros>20:
            calc_alcool=(1.9*litros)
            descon=(5/100)*(calc_alcool)
            print(f'Valor total: {calc_alcool-descon}')
            break
    elif combust=='g':
        if litros<=20:
            calc_gasol=(2.5*litros)
            descon=(4/100)*(calc_gasol)
            print(f'Valor total: {calc_gasol-descon}')
            break
        elif litros>20:
            calc_gasol=(2.5*litros)
            descon=(6/100)*(calc_gasol)
            print(f'Valor total: {calc_gasol-descon}')
            break

