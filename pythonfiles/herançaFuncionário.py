class Funcionario:
    def __init__(self):
        pass
    

    def salario(self):
        nome=input('Nome: ')
        self.nome=nome
        
        cargo=input('Cargo: ')
        self.cargo=cargo
        
        sal=float(input('Salário: R$'))
        self.sal=sal

        imposto=float(input('Quanto (%) de imposto? '))
        self.imposto=(imposto/100)

        beneficio=float(input('Quanto (%) de benefício? '))
        self.beneficio=(beneficio/100)

        self.salFinal=self.sal-((self.sal*self.imposto))+(self.sal*self.beneficio)
        
        
        print(f'\nFuncionário: {self.nome}\n{self.cargo}\nO salário inicial de R${self.sal:.2f}, sob impostos e benefícios, ficou de:\nR${self.salFinal:.2f}')