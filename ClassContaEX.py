class Conta:
    def __init__(self,numero,cpf,nome_titular,saldo):
        
        self.numero = numero
        self.cpf = cpf
        self.nome_titular = nome_titular
        self.saldo = saldo
    
    
    def __depositar__(self,valor):
        self.saldo += valor
    
    def sacar(self,valor):
        self.saldo -= valor
    
    def gerar_extrato(self):
        print(f" Numero: {self.numero}\n Nome: {self.nome_titular}\n CPF: {self.cpf}\n Saldo: R${self.saldo:.2f}")




        