#####       Principais Operações com Strings 

##  O que são Strings?

# Strings são sequências de caracteres utilizadas para armazenar e manipular texto em Python. 
# Elas podem ser definidas com aspas simples (' ') ou duplas (" ").

print("============================== Exemplo de Strings =========================================")
print("")

# a var "texto" recebe o texto "Olá mundo!"
texto = "Olá mundo!"

# Exibirá na tela, o que tem dentro da var "texto"
print(texto) # saída => Olá mundo!

print("")
print("=========================== Principais Operações com Strings  =================================")
print("")

print("==============================  Concatenação  ==============================================")
print("")

# Podemos unir duas ou mais strings utilizando o operador +.

# Variáveis com o nome e sobrenome
nome = "Carlos"
sobrenome ="Silva"

# Junta o nome + sobrenome, dando um espaço " "
nome_completo = nome + " " + sobrenome

# Exibirá na tela a concatenação das Strings
print("Nome completo: \n ",nome_completo) # saída => # Nome completo: Carlos Silva


print("")
print("===================================  Repetição  ==============================================")
print("")

# É possível repetir uma string utilizando o operador *.

# multiplica por 5 o texto "ha" e salva na var "risada"
risada = "ha" * 5

print(risada) # saída => hahahahaha




print("")
print("====================================== Acesso a Caracteres ========================================================")
print("")

# Podemos acessar caracteres de uma string utilizando índices.

# Adiciona o texto "Python" e salva na variável "palavra"
palavra = "Python"

# Exibirá a letra na posição 0
print("Letra do texto, na posição 0: ", palavra[0]) # saída => Letra do texto, na posição 0:  P

# Exibirá a letra na posição -1
print("Letra do texto, na posição -1: ", palavra[-1]) # saída => Letra do texto, na posição -1: n  


print("")
print("==================================== Fatiamento de Strings ===========================================================")
print("")

# Podemos extrair partes de uma string utilizando a sintaxe [início:fim:passo].

#
frase = "Manipulação de Strings"


# Pega "11" letras, na posição "0", e exibi na tela *** Conta os espaços também
print(frase[0:11]) # saída => Manipulação


print(frase[12:]) # saída => de Strings


print(frase[::-1]) # saída => sgnirtS ed oãçalupinaM   *** STRING INVERTIDA


print("")
print("=====================================   Fim    =================================================")
print("")


