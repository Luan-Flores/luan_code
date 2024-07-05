# # serviço fornecedor contas

import codeOficina as fun, os

cad_todos=[]

def cadPessoa():
    
    contatos_lista={()}
    import os
    erro_msg='Tipo de dado inserido inválido '
    
    while True:
        try:
            nome=str(input('Nome: '))
            break
        except ValueError:
            print(erro_msg)
        
    while True:
        try:
            idade=int(input('Idade: '))
            break
        except ValueError:
            print(erro_msg)
    
    while True:
            
            cpf=(input('CPF: '))
            if (cpf.isdigit()) and (len(cpf)==11):
                break
            else:
                print('Digite um CPF válido ')
        
    while True:
        
        tel=(input('Telefone: '))
        if (tel.isdigit()) and (len(tel)>=8):
            
            contatos_lista={(nome,tel)}
            contato=dict(contatos_lista)
            break
        else:
            print('Digite um telefone válido ')
    
        

    os.system('cls')
    print('Nome: {}\nIdade: {}\nCPF: {}\nTelefone: {}'.format(nome,idade,cpf,tel))
    
    cad_lista={
        "nome": nome,
        "idade": idade,
        "telefone": tel,
        "cpf": cpf 
    }
    
    
    cad_todos.append(cad_lista)

while True:
    
    print('\nOficina WGA ')
    opcao_inicial=int(input('Cliente (1)\nVeículos (2)\nPeças (3)\n'))
    
    
    if opcao_inicial==1:
        try:
            opcao=int(input('Cadastro de cliente:\n(1)Novo\n(2)Excluir\n(3)Alterar\n(4)Relatório\n(0)Sair\n'))
            if opcao==0:
                break
        except ValueError:
            print('Tipo de opção inválida')
            os.system('cls')
        if opcao==1:
            print('Cadastro de cliente: ')
            fun.cadPessoa()
            cad_todos
        elif opcao==2:
            fun.excluir_Cadastro()
        elif opcao==3:
            fun.show_Cadastro()
            
    elif opcao_inicial==2:
        try:
            opcao=int(input('Cadastro de veículo:\n(1)Novo\n(2)Excluir\n(3)Alterar\n(4)Relatório\n(0)Sair\n'))
            if opcao==0:
                break
        except ValueError:
            print('Tipo de opção inválida')
            os.system('cls')
        if opcao==1:
            print('Cadastro de veículo: ')
            fun.cadVeiculo()
        
        elif opcao==2:
            fun.excluir_Veiculo()
        elif opcao==3:
            fun.show_car()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida ')
        
            
            