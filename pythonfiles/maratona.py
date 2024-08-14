# ''''''
# while True:
#     try:
#         operacao=int(input('(1) Soma\n(2) Subtração\n(3) Divisão\n(4) Multiplicação\n(0)Sair\n: '))
#         n1=float(input('Primeiro número: '))
#         n2=float(input('Segundo número: '))
#         soma=(n1+n2)
#         subtração=(n1-n2)
#         divisao=(n1/n2)
#         multi=(n1*n2)
        
#         if operacao==1:
#             print(soma)
        
#         elif operacao==2:
#             print(subtração)

#         elif operacao==3:
#             print(divisao)
        
#         elif operacao==4:
#             print(multi)
        
#         elif operacao==0:
#             print('Fim')
#             break
        
#         if soma % 2 == 0 or subtração %2==0 or divisao %2==0 or multi%2==0:
#             print("PAR")
#             print('Inteiro')
        
#         elif soma % 2 != 0 or subtração %2!=0 or divisao %2!=0 or multi%2!=0:
#             print("IMPAR")
#             print('decimal')
#         if soma > 0 or subtração >0 or divisao >0 or multi >0:
#             print('resultado positivo.')
#         elif soma <0 or subtração <0 or divisao <0 or multi<0:
#             print('resultado negativo')
#         elif soma ==0 or subtração==0 or divisao==0 or multi==0:
#             print('ZERO!')
        
    
    

#     except ValueError:
#         print('Inválido')


cont = 0
while True:
    a = input('Telefonou pra vitima:').lower()
    
    if a == ('sim'):
        cont+=1
        break
    elif a == ('nao'):
        break
    else:
        print('Formato Inválido, Por favor, responda com sim ou nao ')
while True:
    b = input('Esteve no local do crime:').lower()
    if b == ('sim'):
        cont+=1
        break
    elif b == ('nao'):
        break
    else:
        print('Formato Inválido, Por favor, responda com sim ou nao ') 
while True:
    c = input('Mora perto da vitima:').lower()
    if c == ('sim'):
        cont+=1
        break
    elif c == ('nao'):
            break
    else:
        print('Formato Inválido, Por favor, responda com sim ou nao ')
while True:
    d = input('Devia pra vitima:').lower()
    if d == ('sim'):
        cont+=1
        break
    elif d == ('nao'):
            break
    else:
        print('Formato Inválido, Por favor, responda com sim ou nao ')
while True:
    e = input('Já trabalhou com a vitima:').lower()
    if e == ('sim'):
        cont+=1
        break
    elif e == ('nao'):
        break
    else:
        print('Formato Inválido, Por favor, responda com sim ou nao ')

if cont < 2:
    print('Inocente')
elif cont == 2:
    print('Suspeito')
elif cont > 2 and cont < 5:
    print('cumplice')
elif cont == 5:
    print('Culpado')

