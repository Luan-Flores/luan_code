def pode_ser_triangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

if pode_ser_triangulo(a, b, c):
    print('Sim, pode ser um triângulo. ')
else:
    print('Não, não pode ser um triângulo. ')
    