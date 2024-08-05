import os
class Pizza:
    def __init__(self):
        pass
    
    def montarPizza(self):
        

            
            
            
            
            
            while True:
                pontosLista={1:'Mal passada',2:'Ao ponto',3:'Bem passada'}
                try:
                    
                    pontoOpc=int(input('Qual o ponto da massa? \n1- Mal passada\n2- Ao ponto\n3- Bem passada'))
                    self.pontoMassa=pontosLista[pontoOpc]
                    print(self.pontoMassa)
                    
                    
                
                except ValueError:
                    print('Inválido')
    
        
    
            # while True:
            #     try:
                    
            #         queijo=input('Qual tipo de queijo? \n1- Mussarela\n2- Ricota\n3- Prato\n4- Cheddar\n5- Minas')
            #         self.queijo=queijo
            #         os.system('cls')
            #         break
                
            #     except ValueError:
            #         print('Inválido')
            # while True:
            #     try:
                    
            #         carne=input('Recheio? \n1- Calabresa\n2- Frango\n3- Carne moída\n4- Ovo')
            #         self.carne=carne
            #         os.system('cls')
            #         break
                
            #     except ValueError:
            #         print('Inválido')            

            # while True:
            #     try:
                    
            #         mato=input('Fitness: \n1- Tomate\n2- Cebola\n3- Salsa')
            #         self.mato=mato
            #         os.system('cls')
            #         break
                
            #     except ValueError:
            #         print('Inválido')
            
            # while True:
            #     try:
            #         opcao=input('Borda recheada? \n1- Sim\n2- Não')
            #         if opcao =='1':
            #             borda=('Recheio: \n1- Catupirico\n2- Cheddar\n3- Chocolate')
            #             self.borda=borda
            #             break
            #         elif opcao =='2':
            #             self.borda=

        
        
        
        
        
        
        
        
