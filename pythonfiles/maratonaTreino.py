#Faça um programa que leia 5 números e informe o maior número.
#Faça um programa que leia 5 números e informe a soma e a média dos números.

# ncount=0
# numeros=[]
# while True:
#     ncount+=1
    
#     nmr=float(input(f'Digite o {ncount}º número: '))
#     numeros.append(nmr)
#     if ncount==5:
#         break

# soma=sum(numeros)


# print(f'Soma dos números: {soma}\nMaior: {max(numeros)}\nMédia: {soma/ncount}')
# lista=['nego','do','borel']

# for i in lista:
#     print(i, end=' ')
# def intervalo(n1,n2):
    
#     if n1<n2:
#         for i in range(n1,n2+1):
#             print(i)
#     elif n1>n2:
#         for i in range(n2,n1+1):
#             print(i)
#     else:
#         print(n1)

# opcao1=int(input('Digite nmr 1: '))
# opcao2=int(input('Digite nmr 2: '))
# intervalo(opcao1,opcao2)
lista_atletas={'nome':1,'luan':0}
atl_4=0
atl_3=0
atl_2=0
atl_1=0
cont=0
while True:
    try:
        atleta=int(input('Número do atleta (1 ao 4): '))
        if (atleta<1 and atleta!=0) or (atleta>23 and atleta!=0):
            continue
        
        elif atleta==0:
            break
        
        elif atleta==1:
            atl_1+=1
            cont+=1
        
        elif atleta==2:
            atl_2+=1
            cont+=1
        elif atleta==3:
            atl_3+=1
            cont+=1
        elif atleta==4:
            atl_4+=1    
            cont+=1
    except ValueError:
        print('Apenas números! ')

pct1=((atl_1*100)/cont)
pct2=((atl_2*100)/cont)
pct3=((atl_3*100)/cont)
pct4=((atl_4*100)/cont)
if pct1==0:
    pct1=0
if pct2==0:
    pct2=0
if pct3==0:
    pct3=0
if pct4==0:
    pct4=0
print(f'Atleta 1: {atl_1} votos ({pct1:.2f}%)\nAtleta 2: {atl_2} votos ({pct2:.2f}%)\nAtleta 3: {atl_3} votos ({pct3:.2f}%)\nAtleta 4: {atl_4} votos ({pct4:.2f}%)')
