import os
class conta():
    def __init__(self):
       pass
    
    
    def cadGeral(self):
        while True:
            nome=input('Nome: ')
            if nome.isdigit()==True or nome=='':
                print('Inválido. ')
            else:
                self.nome=nome
                break
        while True:
            try:
                cpf=(input('CPF: '))
                if cpf==''  or  len(cpf)!=11:
                    print('inválido')
                else:
                    self.__cpf=cpf
                    break
            except ValueError:
                print('Dado inserido inválido')
        while True:
            try:
                senha=input('Crie uma senha: ')
                if senha=='':
                    print('Inválido. ')
                else:
                    self.__senha=senha
                    break
            except ValueError:
                print('Dado inserido inválido.')
        
        while True:
            try:
                saldo=float(input('Qual o saldo? R$'))
                self.__saldo=saldo
                break
            except ValueError:
                print('Dado inserido inválido')
                continue
        
    
    
    def extrato(self):
            try:
                senha=input('Digite a senha: ')
                
                if senha!=self.__senha:
                    print('Senha inválida. ')
                    return False
                
                elif senha==self.__senha:
                    print(f'Saldo: R${self.__saldo:.2f}')
                    return True
              
            except ValueError:
                print('Dado inserido inválido')
                return False
    
    def depositar(self):
            try:
                valorDep=float(input('Quanto quer depositar? R$'))
                
                if valorDep <= 0:
                    print('Digite qualquer valor acima de R$0')
                    return False
                else:
                    self.__saldo+=valorDep
                    print(f'Depósito de R${valorDep:.2f} concluído ')
                    return True
            
            except ValueError:
                print('Dado inserido inválido')
                return False
    
    def sacar(self):
            try:
                senha=input('Digite a senha: ')
                
                if senha!=self.__senha:
                    print('Senha inválida. ')
                    return False
                
                if senha==self.__senha:
                    
                        while True:
                            try:
                                
                                valorSaq=float(input(f'Saldo: R${self.__saldo:.2f}, qual o valor do saque? R$'))
                        
                                if valorSaq==0:
                                    print('Digite um valor acima de R$0')
                                    continue
                                
                                elif valorSaq <= self.__saldo:
                                    self.__saldo-=valorSaq
                                    os.system('cls')
                                    print(f'Saque de R${valorSaq:.2f} concluído')
                                    
                                    break
                                
                                elif valorSaq > self.__saldo:
                                    os.system('cls')
                                    print(f'O valor R${valorSaq} excede o saldo total da conta. ')
                                    continue
                            except ValueError:
                                os.system('cls')
                                print('Dado inserido inválido')
            
                        return True

            except ValueError:
                print('Dado inserido inválido')
                return False
    