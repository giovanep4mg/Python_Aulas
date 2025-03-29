############               Conjuntos em Python
##     Um conjunto (set) é uma coleção de elementos únicos.

print("================================================= Criando um conjunto ========================================")
print("")
##  Criando um conjunto

# Cria um conjuto  "numeros"
numeros = {1,2,3,4,5,6,7,8,9,10}

# Exibir na tela 
print(f"Exibindo o conjunto criado: {numeros}") # Exibindo o conjunto criado: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print()
print("================================================= Adicionando elementos ========================================")
print("")

# Adiciona o valor "15" dentro do conjunto "numeros"
numeros.add(15)

#  Exibir na tela 
print(f"Atualizando, adicionando elementos no conjunto : {numeros}")
# Atualizando, adicionando elementos no conjunto : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15}


print()
print("================================================= Removendo elementos ========================================")
print("")

# Remove o valor "3" de dentro do conjunto "numeros"
numeros.remove(3)

#  Exibir na tela 
print(f"Atualizando, removendo elementos no conjunto : {numeros}")
# Atualizando, removendo elementos no conjunto : {1, 2, 4, 5, 6, 7, 8, 9, 10, 15}

print()
print("================================================= União de conjuntos ========================================")
print("")

# Criei um conjunto com números pares
impares = {1,3,5,7,9}

# Criei um conjunto com números pares
pares = {2,4,6,8,}

# Usando o "union()", unimos os dois conjuntos
resultado_uniao = impares.union(pares)

# Exibir na tela
print(f"Resultado união: {resultado_uniao}") # Resultado união: {1, 2, 3, 4, 5, 6, 7, 8, 9}


print()
print("================================================= Interseção de conjuntos ========================================")
print("")

#
resultado_insercao = pares.intersection(pares)

print("Resultado inserção: ", resultado_insercao) # Resultado inserção:  {8, 2, 4, 6}



print()
print("================================================= Diferença entre conjuntos ========================================")
print("")


# Vai separar os diferentes "pares", do conjunto "impares" e salvar na var "resultado_diferenca"
resultado_diferenca = impares.difference(pares)

# Exibir na tela
print("Resultado diferença: ", resultado_diferenca) # Resultado diferença:  {1, 3, 5, 7, 9}


print()
print("=============================== Verificando a existência de um elemento em um conjunto ===================================")
print("")

# Criando um conjunto, com vários números
numeros1 = {1,2,3,4,5,6,7,8,9,10} # Conjunto Números 2:  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Exibir na tela
print("Conjunto Números 2: ",numeros1)


#   Vai verificar se existe o número "4" dentro co conjunto "numeros1", se tiver retorna "True"
print("Resultado da busca: ",4 in numeros1) # Resultado da busca:  True


print()
print("================================================= FIM   ========================================")
print("")