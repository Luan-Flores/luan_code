# from ClassControle import*

# remote_control_UM = ControleRemoto('Azul',30,3,5)
# remote_control_DOIS = ControleRemoto('preto',35,2,5)

# print(remote_control_UM.cor)
# print(remote_control_DOIS.cor)

# remote_control_UM.mudar_canal('+')
saldo=230
# senhacerta='larga'
# def extrato():
#         while True:
#             try:
#                 senha=input('Digite a senha: ')
#                 if senha!=senhacerta:
#                     print('Senha inválida. ')
#                 elif senha==senhacerta:
#                     print(f'Saldo: R${saldo:.2f}')
#                     break
            
            
#             except ValueError:
#                 print('Dado inserido inválido')
# extrato()

def depositar():
        global saldo
        saldo=230
        while True:
            try:
                valorDep=float(input('Quanto quer depositar? R$'))
                if valorDep<0:
                    print('Digite qualquer valor acima de R$0')
                else:
                    saldo+=valorDep
                    print(f'O depósito de R${valorDep:.2f} foi concluído ')
                    print(saldo)
            except ValueError:
                print('Dado inserido inválido')
depositar()
