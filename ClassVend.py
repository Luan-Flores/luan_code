class Vendedor():
    def __init__(self,x,y):
        
        self.nome=x 
        self.vendas=y


nome_random='zeca urubis' # nome_random -> x
vendas_random=1200   # vendas_random -> y


vendedor_Um=Vendedor(nome_random,vendas_random)#  ->  (x,y)


print('vendedor: {}'.format(vendedor_Um.nome)) #  OU  print(vendedor_Um.nome)

print(vendedor_Um.vendas)