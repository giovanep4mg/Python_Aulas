#### Exercícios Listas e Tuplas

print("")
print("============================= 1. Crie uma lista com cinco números e exiba o maior valor. ===========================")
print("")

# 1. Crie uma lista com cinco números e exiba o maior valor.

# Criando uma lista com 5 números
lista_numeros = [1,34,89,21,12,]

# Exibir a lista criada
print(f"Lista criada: {lista_numeros}") # saída => Lista criada: [1, 34, 89, 21, 12]

# Pega o item na posição 2, e salva na variável
maior_valor = lista_numeros[2]

# Exibir na tela o maior número selecionado da lista
print(f"O número de maior valor é o {maior_valor}") # saída => O número de maior valor é o 89


print("")
print("=========================== 2. Crie uma tupla com três nomes e exiba o segundo nome. ===========================")
print("")

# Criando uma Tupla
nomes = ("Giovani","Maria","João") # saída => Tupla criada: ('Giovani', 'Maria', 'João')

# Exibir a Tupla criada
print(f"Tupla criada: {nomes}")

# Seleciona o item na posição 1, dentro da Tupla que foi criada e salva na var "segundo_nome"
segundo_nome = nomes[1]

# Exibi na tela 
print(f"Segundo nome da Tupla: {segundo_nome}") # saída => Segundo nome da Tupla: Maria


print("")
print("================================ 3. Inverta a ordem dos elementos de uma lista. =============================")
print("")


# Criando uma lista de frutas
frutas = ["banana","maça","pera","uva","jaboticaba","melão"] 

# saída => Lista criada: ['banana', 'maça', 'pera', 'uva', 'jaboticaba', 'melão']


# Exibi a lista criada
print(f"Lista criada: {frutas}")

# Usando o "reverse" para inverter a ordem da lista, o primeiro item será o último
frutas.reverse()

# Exibir
print(f"Lista invertida: {frutas}")

# saída => Lista invertida: ['melão', 'jaboticaba', 'uva', 'pera', 'maça', 'banana']



print("")
print("============================ 4. Adicione um novo elemento a uma tupla sem modificar a original. =====================")
print("")

#Criando uma Tupla
nomes_tupla = ("Pedro","João","Franciso")

# Exibir a tupla criada
print(f"Tupla criada: {nomes_tupla}") # saída => Tupla criada: ('Pedro', 'João', 'Franciso')

# Adiciona * uma nova tupla "("Maria",)"  a tupla já criada, se tornam uma só, e salva na variável "nomes_tupla_atualizada"
nomes_tupla_atualizada = nomes_tupla +  ("Maria",)

# Adicionou uma nova tupla + a antiga tupla, assim não modificou a original

# Exibir na tela
print(f"Tupla atualizada: {nomes_tupla_atualizada}") # saída => Tupla atualizada: ('Pedro', 'João', 'Franciso', 'Maria')


print("")
print("================================== 5. Concatene duas listas e exiba o resultado. ===============================")
print("")

# Pegando uma lista já criada, e exibindo na tela
print(f"Lista frutas: {frutas}") # saída => Lista frutas: ['melão', 'jaboticaba', 'uva', 'pera', 'maça', 'banana']

print(f"Lista números: {lista_numeros}") # saída => Lista números: [1, 34, 89, 21, 12]

# Junta a lista frutas + lista_numeros e salva na variável "concatenar"
concatenar = frutas + lista_numeros


print(f"Listas concatenadas: {concatenar}") 
# saída => Listas concatenadas: ['melão', 'jaboticaba', 'uva', 'pera', 'maça', 'banana', 1, 34, 89, 21, 12]


print("")
print("============================================ FIM ============================================================")
print("")


