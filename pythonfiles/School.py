
def media():
    dict_alunos={}
    while True:
        nome=input('Nome do aluno: ')
        if nome =='':
            break
        
        while True:
            try:
                
                nota=float(input('Nota: '))
                if nota < 0 or nota > 10:
                    print('Inválido. ')          
            
            except ValueError:
                break
    
    for nome in sorted(dict_alunos.keys()):
     adiçao = 0
     contador = 0
    for score in dict_alunos[nome]:
         adiçao += score
         contador += 1
    print(nome, ":", adiçao / contador)

media()




# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
# 	    break
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)
