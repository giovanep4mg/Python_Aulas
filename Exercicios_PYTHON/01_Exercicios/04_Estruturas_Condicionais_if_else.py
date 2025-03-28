###   4. Estruturas Condicionais (if/else)

print("================================== Exercício 1 =========================================")
#   Exercício 11: Peça um número e diga se ele é positivo, negativo ou zero.

# Pedir um número ao usuário
num1 = 10 # int(input("Digite um número:"))   # Travado para pedir nada

# Se o "num1" for maior que 0, executa a ação abaixo...
if num1 > 0:
    print(f"O número {num1}, é positivo!")
    
# Se "num1" for menor que 0, executa a ação abaixo...
elif num1 < 0:
    print(f"O número {num1}, é negativo!")

# Se "num1" for igual a 0, executa a ação abaixo...
elif num1 == 0:
    print(f"O número {num1}, é zero!")
    

print("================================== Exercício 2 =========================================")
#   Exercício 12: Verifique se um ano informado pelo usuário é bissexto.

# Usuário adiciona o ano 
ano = 1988 # int(input("Digite o ano:")) #Travado para não pedir ao usuário para inserir o ano

#   Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400. 
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano de {ano} é bissexto!")
else:
    print(f"O ano de {ano} não é bissexto!")

print("================================== Exercício 2 =========================================")
#   Exercício 13: Peça dois números e informe qual é o maior.

# Pedir ao usuário que adicione os números
numero1 = 19 # int(input("Digite um número:"))  travado para não pedir ao usuário
numero2 = 23 # int(input("Digite um número:")) travado para não pedir ao usuário

# Se o "numero1" for maior que o "numero2", vai executar a ação abaixo
if numero1 > numero2:
    print(f"O número {numero1} é o maior!")
else:
    print(f"O número {numero2} é o maior!")
    
    

print("================================== Exercício 3 =========================================")
#   Exercício 14: Peça a idade do usuário e diga se ele pode votar.

# Pedir ao usuário para adicionar a sua idade
idade = 18 # int(input("Digite sua idade:")) travado para não pedir ao usuário 

# 
if idade >= 16:
    print(f"Você tem {idade} anos, já pode votar!")
else:
    print(f"Você tem {idade} anos, não pode votar!")
    
    

print("================================== Exercício 4 =========================================")
#   Exercício 15: Peça ao usuário uma senha e valide se é igual a "1234".

#   Pedir ao usuário para adicionar a senha
senha = 1234 # int(input("Digite sua senha:"))  travado para não pedir ao usuário


#
if senha == 1234:
    print("Sua senha está correta!")
else:
    print("Erro, sua senha está incorreta!")
    
    

print("====================================== FIM =========================================")