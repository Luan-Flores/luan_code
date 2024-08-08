from PizzaCode import*
pizza=Pizza()
print('Pizzaria 141')
while True: 
    opc=input('1- Pedir pizza\n2- Pedidos\n3- Cadastrar cliente\n0- Sair')
    if opc=='1':        
        process=pizza.montarPizza()     
        break
    elif opc=='2':
        #histórico
        break

            