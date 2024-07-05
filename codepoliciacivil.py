class Policia():
    def __init__(self):
        pass
        


    def cadPolicia(self):
        while True:
            nome=input('Nome: ')
            if nome.isdigit()==True or nome=='':
                print('Inválido. ')
            else:
                self.nome=nome
                break
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
                matricula=input('Matrícula: ')
                if matricula=='':
                    print('Inválido. ')
                else:
                    self.matricula=matricula
                    break
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                telefone=input('Telefone: ')
                if (telefone.isdigit()) and (len(telefone)>7):
                    self.__telefone=telefone
                    break
                else:
                    print('Digite um telefone válido ')
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                email=input('Email: ')
                if len(email)<10:
                    print('Digite um email válido. ')
                else:
                    self.__email=email
                    break
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                endereco=input('Endereço: ')
                if endereco=='':
                    print('Digite um endereço válido ')
                else:
                    self.__endereco=endereco
                    break
            except ValueError:
                print('Dado inserido inválido.')
    
    
    def cadBO(self):
        while True:
            try:
                tipo=input('Tipo de ocorrência: ')
                if tipo=='' or tipo.isdigit()==True:
                    print('Digite uma ocorrência válida')
                else:
                    self.tipo=tipo
                    break
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                acusado=input('Nome do suspeito: ')
                if acusado=='' or acusado.isdigit()==True:
                    print('Digite um nome válido')
                else:
                    self.acusado=acusado
                    break
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                vitima=input('Nome da vítima: ')
                if vitima=='' or vitima.isdigit()==True:
                    print('Digite um nome válido')
                else:
                    self.__vitima=vitima
                    break
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                telefonevit=input('Telefone da vítima: ')
                if (telefonevit.isdigit()) and (len(telefonevit)>7):
                    self.__telefonevit=telefonevit
                    break
                else:
                    print('Digite um telefone válido ')
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                emailvit=input('Email: ')
                if len(emailvit)<10:
                    print('Digite um email válido. ')
                else:
                    self.__emailvit=emailvit
                    break
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                enderecovit=input('Endereço: ')
                if enderecovit=='':
                    print('Digite um endereço válido ')
                else:
                    self.__enderecovit=enderecovit
                    break
            except ValueError:
                print('Dado inserido inválido.')
        
    def cadPreso(self):
        while True:
            nomepreso=input('Nome do Preso: ')
            if nomepreso.isdigit()==True or nomepreso=='':
                print('Inválido. ')
            else:
                self.__nomepreso=nomepreso
                break
        while True:
            try:
                motivo=input('Motivo da prisão: ')
                if motivo=='':
                    print('Inválido. ')
                else:
                    self.__motivo=motivo
                    break
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                nascimentopreso=str(input('Data de nascimento (Utilize apenas números): '))
                if len(nascimentopreso)!=8 :
                    print('Inválido. ')
                else:
                    self.__nascimentopreso=nascimentopreso
                    break
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                sexo=input('Sexo: \n(1)Masculino (2)Feminino')
                if sexo=='1':
                    self.__sexo='Masculino'
                    break
                if sexo=='2':
                    self.__sexo='Feminino'
                    break
                else:
                    print('Digite 1 ou 2')
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                enderecopreso=input('Endereço: ')
                if enderecopreso=='':
                    print('Digite um endereço válido ')
                else:
                    self.__enderecopreso=enderecopreso
                    break
            except ValueError:
                print('Dado inserido inválido.')
        while True:
            try:
                condenacao=input('Condenação: ')
                if condenacao=='':
                    print('Inválido')
                else:
                    self.__condenacao=condenacao
                    break
            except ValueError:
                print('Dado inserido inválido.')
    

    def showBO(self):
        try:
            print(f'Boletim de Ocorrência\nTipo: {self.tipo}\nAcusado: {self.acusado}\nVítima: {self.__vitima}\nTelefone da Vítima: {self.__telefonevit}\nEmail da Vítima: {self.__emailvit}\nEndereço: {self.__enderecovit}')
            return True
        except:
            print('Inválido')
            return False

    def showPol(self):
        try:
            print(f'Policiais\nNome: {self.nome}\nSenha: {self.__senha}\nMatrícula: {self.matricula}\nTelefone: {self.__telefone}\nEmail: {self.__email}\nEndereço: {self.__endereco}')
            return True
        except:
            print('Inválido')
            return False
    
    def showPreso(self):
        try:
            print(f'Presos\nNome: {self.__nomepreso}\nAcusação: {self.__motivo}\nNascimento: {self.__nascimentopreso}\nSexo: {self.__sexo}\nEndereço: {self.__enderecopreso}\nCondenação: {self.__condenacao}')
            return True
        except:
            print('Inválido')
            return False
        
        
        