# def pode_ser_triangulo(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# a = float(input('Primeiro lado: '))
# b = float(input('Segundo lado: '))
# c = float(input('Terceiro lado: '))

# if pode_ser_triangulo(a, b, c):
#     print('Sim, pode ser um triângulo. ')
# else:
#     print('Não, não pode ser um triângulo. ')
# Define the initial populations and growth rates
P_A0 = 80000
r_A = 0.03
P_B0 = 200000
r_B = 0.015

# Initialize the time variable
t = 0

# Iterate until the population of A is greater than or equal to the population of B
while P_A0 * (1 + r_A)**t < P_B0 * (1 + r_B)**t:
    t += 1

print(t)