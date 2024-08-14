class Loja_Tenis():
    def __init__(self):
        while True:
            try:
                self.nome=input('Nome: ')
                break
            except ValueError:
                print('Inválido, tente outra vez. ')
        while True:
            try:
                
                self.idade=(input('Idade: '))
                
                if self.idade.isdigit()== True:
                    break
                else:
                    print('Digite apenas números. ')
            
            except ValueError:
                print('Inválido, tente outra vez. ')
        
        while True:
            try:
                
                self.sexo=input('Sexo: (1)Masculino (2)Feminino ')
                if self.sexo=='1':
                    self.sexo='Masculino'
                    break
                elif self.sexo=='2':
                    self.sexo='Feminino'
                    break
                else:
                    print('Inválido, use 1 (Masculino) ou 2 (Feminino). ')
            
            except ValueError:
                print('Inválido, tente outra vez')
        while True:
            try:
                self.tamanho=int(input('Qual número você calça? (Digite um número entre 12 e 48) '))
                if self.tamanho<12 or self.tamanho>48:
                    print('Tamanho inválido, tente novamente. ')
                else:
                    break
            except ValueError:
                print('Inválido, tente outra vez. ')
            
        
    
    def show_Cad(self):
        print(f" Nome: {self.nome}\n Idade: {self.idade}\n Sexo: {self.sexo}\n Tamanho: {self.tamanho}")
