from herançaRaio import*
import os

raio=float(input('Qual o raio do círculo? (em cm)'))

x=Círculo(raio)

os.system('cls')

print(f'Área do círculo de raio {raio:.0f} cm: {x.area()} cm²')
print(f'Perímetro do círculo de raio {raio:.0f} cm: {x.perimetro()} cm')
