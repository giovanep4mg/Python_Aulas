#######    Operações com Listas

print("======================================== Acessando Elementos ========================================================")
print("")
###   Acessando elementos da lista 

# Criando uma lista de frutas
frutas = ["banana","maça","uva","pera"]

print(f"Lista frutas: {frutas}")

# Seleciona dentro da lista frutas na posição [x]
print(f"Lista frutas, posição 0 : {frutas[0]}") # saída => banana
print(f"Lista frutas, posição -1 : {frutas[-1]}") # saída => pera


print("")
print("======================================== Modificando Elementos ========================================================")
print("")
###     Modificando elementos 

# Lista de nomes com nomes já adicionados
nomes =["João","Pedro","Marcos"]

print(f"Lista nomes: {nomes}") # saída => Lista nomes: ['João', 'Pedro', 'Marcos']

# Modificando a lista, troca o nome "Pedro" por esse outro nome "Maria"
nomes[1] = "Maria"

#
print(f"Nomes atualizada: {nomes}") # saída => Nomes: ['João', 'Maria', 'Marcos']


print("")
print("======================================== Adicionando Elementos ========================================================")
print("")

# Lista com nomes de cidades
cidades = ["Passa-Quatro","São Paulo","Itanhandu","Itamonte"]

# Exibir na tela
print(f"Lista cidades: {cidades}") # saída => Lista cidades: ['Passa-Quatro', 'São Paulo', 'Itanhandu', 'Itamonte']

# adiciona "Cruzeiro" no final da lista
cidades.append("Cruzeiro")

#
print(f"Lista cidades, atualizada: {cidades}") 
# saída => Lista cidades, atualizada: ['Passa-Quatro', 'São Paulo', 'Itanhandu', 'Itamonte', 'Cruzeiro']

# Adiciona "Rio", na posição 2 da lista cidades
cidades.insert(2, "Rio")

#
print(f"Lista cidades, atualizada 2: {cidades}")  
# saída => Lista cidades, atualizada 2: ['Passa-Quatro', 'São Paulo', 'Rio', 'Itanhandu', 'Itamonte', 'Cruzeiro']

print("")
print("======================================== Removendo  Elementos ========================================================")
print("")

# lista 
animais = ["cachorro","gato","porco"]

print(f"Lista animais: {animais}") # Lista animais: ['cachorro', 'gato', 'porco']

# Removendo da lista animais "porco"
animais.remove("porco")

print(f"Lista animais, removendo 'porco' : {animais}") # Lista animais, removendo 'porco' : ['cachorro', 'gato']

# Vai remover o último item da lista animais, e salvar na var "ultimo"
ultimo = animais.pop()

print(f"Lista animais: {ultimo}") # Lista animais: gato


print(f"Lista animais, sobrou: {animais}") # Lista animais, sobrou: ['cachorro']


print("")
print("===============================================  FIM  ====================================================================")
print("")