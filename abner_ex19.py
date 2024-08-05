#019
#numero1 = int(input("\ndigite um numero: "))
# numero2 = int(input("digite outro numero: "))

# if (numero1 > numero2):
#     print("numero {0} maior".format(numero1))
# else:
#     print("numero {0} maior".format(numero2))


# 021
# x = input("Digite uma letra: ")
# x = x.upper()
# if x == 'F':
#     print("F - Feminino")
# elif x == "M":
#     print("M - Masculino")
# else:
#     print("Sexo Inválido")

#023
# n1= float(input("Digite sua primeira nota: "))
# n2=float(input("Digite sua segunda nota: "))

# media= (n1+n2)/2

# if media >= 7 and media < 10:
#     print("Aprovado!")

# elif media < 7:
#     print("Reprovado.")

# elif media == 10:
#     print("Aprovado com Distinção.")

#032
# n1= float(input("Digite sua primeira nota: "))
# n2=float(input("Digite sua segunda nota: "))

# media= (n1+n2)/2

# if media >= 9 and media <= 10:
#     print("APROVADO: A")

# elif media >= 7.5 and media < 9:
#     print("APROVADO: B")

# elif media >= 6 and media < 7.5:
#     print("APROVADO: C")

# elif media >= 4 and media < 6:
#     print("REPROVADO: D")

# elif media < 4:
#     print("REPROVADO: E")

#015
# valor_hora = float(input("qual valor da sua hora de trabalho? "))
# horas_trabalhadas = int(input("quantas horas você trabalha por mes? "))

# salario_bruto = valor_hora * horas_trabalhadas

# ir  = 0.11 * salario_bruto
# inss = 0.08 * salario_bruto
# sindicato = 0.05 * salario_bruto
# descontos = ir + inss + sindicato
# salario_liquido = salario_bruto - descontos
# print("\n+ Salário Bruto : R$ {0:.2f}".format(salario_bruto))
# print("- IR (11%): R$ {0:.2f}".format(ir))
# print("- INSS (8%): R$ {0:.2f}".format(inss))
# print("- Sindicato (5%): R$ {0:.2f}".format(sindicato))
# print("= Salário Liquido : R$ {0:.2f}".format(salario_liquido))

#014
 
peso_peixes = int(input("Informe o peso dos peixes (KG): "))

if peso_peixes > 50:
    peso_excedente = peso_peixes - 50
    multa = peso_excedente * 4
    print("Quantidade excedente: ", peso_excedente)
    print("Multa: R$", multa)
else:
    print("Parabens, esta abaixo de 50kg")