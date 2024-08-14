from ClassEncapsulamentoEX import*
opc=None
while True:
    print('\t---Banco 123---')
    while True:
        opc=input('     (1) Cadastro (0) Sair')
        if opc=='0':
            break
        if opc=='1':
            
            x=conta()
            x.cadGeral()
            
            while True:
                print(f'Olá, {x.nome}')
                opcaoConta=input('(1)Extrato\n(2)Depositar\n(3)Sacar\n(0)Sair')
                
                if opcaoConta=='0':
                    break
                
                if opcaoConta=='1':
                    while True:
                        extrato=x.extrato()
                        if extrato==False:
                            continue
                        break
                
                elif opcaoConta=='2':
                    while True:
                        deposito=x.depositar()
                        if deposito==False:
                            continue
                        break
                
                elif opcaoConta=='3':
                    while True:
                        saque=x.sacar()
                        if saque==False:
                            continue
                        break

                
                
