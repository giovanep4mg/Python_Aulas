####  Estruturas Condicionais (if/else)

# Estrutura básica do if/else

# variável "nome" recebe o valor de => 18
idade = 18

# Se o valor da variável "idade" for maior ou igual a 18
if idade >= 18:
    # Exibi essa mensagem, se for maior ou igual a 18
    print("Você é maior de idade!")

# Se não..
else:
    # Senão for, vai exibir essa outra mensagem
    print("Você é menor de idade!")
    
print("--------------------------------  Usando ` elif ` para Múltiplas Condições ------------------------------------------")
###### Usando "elif" para Múltiplas Condições

# variável "nota" recebe o valor de => 75
nota = 75

# SE, o valor da var "nota" for maior ou igual a "90"
if nota >= 90:
    # Exibirá essa mensagem
    print("Nota A, excelente!")
elif nota >= 80:
    print("Nota B, muito bom!")
elif nota >= 70:
    print("Nota C, bom!")
elif nota >= 60:
    print("Nota D, aprovado!")
else:
    print("Nota F, reprovado!")
    

print("--------------------------------  Uso de if/else com Operadores Lógicos ------------------------------------------")
######   Uso de if/else com Operadores Lógicos

# Variável "idade2" recebe o valor de => 20
idade2 = 20

# Variável "tem_carteira" recebe o valor booleano => True => Verdadeiro
tem_carteira = True

# se o valor da var "idade2" for maior ou igual a 18, e se valor da var "tem_carteira" for "True"
if idade2 >= 18 and tem_carteira:
    print("Pode dirigir!")
else:
    print("Não pode dirigir!")
    
print("--------------------------------  Operador Ternário ( if em uma linha) ------------------------------------------")
#######   Operador Ternário ( if em uma linha)
    
# Variável recebe o valor de 20
idade3 = 20

# faz a verificação se a idade é maior ou igual a 18, e salvará na var "status" o resultado
status = "Maior de idade! " if idade3 >= 18 else "Menor de idade!"

print(status)

print("--------------------------------  Exemplo Prático: Verificando Número Par ou Ímpar  ------------------------------------------")
#####   Exemplo Prático: Verificando Número Par ou Ímpar

#
#     numeroUsuario = int(input("Diigite um número:"))

numeroUsuario = 25


#
if numeroUsuario % 2 == 0:
    print(f"O número {numeroUsuario} é par!")
else:
    print(f"O número {numeroUsuario} é impar!")
    
    
print("--------------------------------  Exemplo com Múltiplas Condições ------------------------------------------")
###### Exemplo com Múltiplas Condições


#
#   idade4 = int(input("Digite sua idade:"))

#
idade4 = 39

if idade4 < 12:
    print("Você é uma criança.")
elif idade4 < 18:
    print("Você é um adolescente.")
elif idade4 < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
    

