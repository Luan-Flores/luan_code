from codepoliciacivil import*
import os
pc=Policia
opc=None
while True:
    print('\t-/- 141ª Delegacia da Polícia Civil -/-')
    opc=input('(1)Cadastrar Boletim de Ocorrência\n(2)Cadastrar Agente\n(3)Cadastrar Presidiário\n(4)Relatórios \n(0)Sair\n')
    if opc=='0':
        break
    if opc=='1':
        print('Cadastro de Boletim de Ocorrência')
        pc.cadBO(pc)
        os.system('cls')
        continue
    if opc=='2':
        print('Cadastro de novo Agente')
        pc.cadPolicia(pc)
        os.system('cls')
        continue
    if opc=='3':
        print('Cadastro de novo Detento:')
        pc.cadPreso(pc)
        os.system('cls')
        continue
    if opc=='4':
        while True:
            print('\t-/- 141ª Delegacia da Polícia Civil -/-\nRelatório:')
            opcRel=input('(1)Boletim de Ocorrência\n(2)Policiais\n(3)Detentos\n(0)Sair\n')
            if opcRel=='0':
                break
            if opcRel=='1':
                while True:
                    os.system('cls')
                    showBO=pc.showBO(Policia)
                    if showBO==False:
                        os.system('cls')
                        print('Boletim de Ocorrência não consta.')
                    opcDentro=input('(0) Sair')
                    if opcDentro=='0':    
                        os.system('cls')
                        break
            if opcRel=='2':
                while True:
                    os.system('cls')
                    showPol=pc.showPol(Policia)
                    if showPol==False:
                        os.system('cls')
                        print('Policial não consta.')
                    opcDentro=input('(0) Sair')
                    if opcDentro=='0':
                        os.system('cls')
                        break
            if opcRel=='3':
                while True:
                    os.system('cls')
                    showPreso=pc.showPreso(Policia)
                    if showPreso==False:
                        os.system('cls')
                        print('Preso não consta.')
                    opcDentro=input('(0) Sair')
                    if opcDentro=='0':
                        os.system('cls')
                        break

    
    

