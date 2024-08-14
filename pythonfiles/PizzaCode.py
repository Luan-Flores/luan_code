import os
class Pizza:
    queijos_pizza={
            '1':'Mussarela',
            '2':'Ricota',
            '3':'Prato',
            '4':'Cheddar',
            '5':'Minas'
                }
    pontos_pizza = {
            '1': 'Mal passada',
            '2': 'Ao ponto',
            '3': 'Bem passada'}
    matos_pizza={
            '1':'Tomate',
            '2':'Cebola',
            '3':'Salsa'
        }
    carnes_pizza={
            '1':'Calabresa',
            '2':'Frango',
            '3':'Carne seca',
            '4':'Ovo'
            }
            
    def __init__(self):
        pass
    
    def montarPizza(self):
            pizza_todas=[]
            self.pizzatodas=(pizza_todas)
            pizza_unidade=[]
            
            while True:
                
                try:
                    
                    pontoOpc=str(input('Qual o ponto da massa? \n1- Mal passada\n2- Ao ponto\n3- Bem passada\n'))
                    if pontoOpc != '1' and pontoOpc != '2' and pontoOpc !='3':
                        print('Escolha inválida')
                        
                    
                    else:
                        
                        PontoMassa = {"Ponto da Massa": self.pontos_pizza[pontoOpc]}
                        pizza_unidade.append(PontoMassa)
                        self.ponto=PontoMassa
                        break
                    
                    
                except ValueError:
                    print('Inválido')
    
            
            while True:
                try:
                    
                    QueijoOpc=input('Qual tipo de queijo? \n1- Mussarela\n2- Ricota\n3- Prato\n4- Cheddar\n5- Minas\n')
                    if QueijoOpc!='1' and QueijoOpc!='2' and QueijoOpc!='3' and QueijoOpc != '4' and QueijoOpc !='5':
                        print('Escolha inválida')
                    else:
                        queijo_da_pizza={'Queijo': self.queijos_pizza[QueijoOpc]}
                        pizza_unidade.append(queijo_da_pizza)
                        self.queijo=queijo_da_pizza
                        break
                
                except ValueError:
                    print('Inválido')

            
            while True:
                try:
                    
                    CarneOpc=input('Recheio? \n1- Calabresa\n2- Frango\n3- Carne seca\n4- Ovo')
                    if CarneOpc != '1' and CarneOpc != '2' and CarneOpc !='3' and CarneOpc !='4':
                        print('Escolha inválida')
                    else:
                        carne_recebe={'Carne':self.carnes_pizza[CarneOpc]}
                        pizza_unidade.append(carne_recebe)
                        self.carne=carne_recebe
                        break
                
                except ValueError:
                    print('Inválido')            
            
          
            while True:
                try:
                    
                    MatoOpc=input('Fitness: \n1- Tomate\n2- Cebola\n3- Salsa')
                    if MatoOpc != '1' and MatoOpc!='2' and MatoOpc!='3':
                        print('Escolha inválida')
                    else:
                        mato_recebe={'Mato':self.matos_pizza[MatoOpc]}
                        pizza_unidade.append(mato_recebe)
                        self.mato=mato_recebe
                        break
                except ValueError:
                    print('Inválido')
            pizza_todas.append(pizza_unidade)

    def mostrar_pizza(self):
        print(self.pizzatodas)