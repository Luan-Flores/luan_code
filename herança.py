class Pessoa:
    
    def __init__(self,nome,idade,endereco,cidade,estado):
        self.nome=nome
        self.idade=idade
        self.endereco=endereco
        self.cidade=cidade
        self.estado=estado


    def relatorio(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Endereço: {self.endereco}')
        print(f'Cidade: {self.cidade}')
        print(f'Estado: {self.estado}')

class Aluno(Pessoa):
    def __init__(self, mensalidade, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.mensalidade=mensalidade
        print('---------------------')
        print('seja bem-vindo querido aluno')
        super().relatorio
        print(f'mensalidade: {self.mensalidade}')
        print('---------------------')

# Pessoa('luan','18','rua barao','maringá','paranel').__init__

class Professor(Pessoa):
    def __init__(self, salario, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.salario=salario
        print('---------------')
        print('seja bem-vindo querido professor')
        super().relatorio()
        print(f'salário: {salario}')
        print('---------------')
# Professor('2300','luan','18','rua barao','maringá','paranel').__init__