class Aluno:
    def __init__(self):
        pass
        
    
    def fill(self):
        import os
        nome=input('Nome: ')
        self.nome=nome
        
        matricula=input('Matrícula: ')
        self.matricula=matricula
        
        s=1
        count=0
        notas=[]
        while True:
            
            try:
                os.system('cls')
                count+=s
                nota=float(input(f'(Digite nada para sair) \nNota {count}: '))
                notas.append(nota)
                self.notas=notas
            
            except ValueError: 
                os.system('cls')
                break
           
        print(f'Notas do aluno {self.nome}: \n{self.notas}')
                
    
    def mediaNotas(self):
        soma=0
        cont=0
        
        for nota in self.notas:
            cont+=1
            self.cont=cont
        
        
        
        for nota in self.notas:
            soma += nota
            self.soma=soma
        

        self.media=((self.soma)/self.cont)
        
        
        print(f'A média das notas do aluno {self.nome} é: {self.media:.2f}')
            
