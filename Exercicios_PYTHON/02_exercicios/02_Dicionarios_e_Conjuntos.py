####### Dicionários e Conjuntos

print("")
print("================ 1. Crie um dicionário com três pares chave-valor e exiba um dos valores. =============")
print("")

# Criando um dicionário
dicionario1 = {
    "nome" : "Giovani",
    "idade" : "23",
    "cidade" : "P4"
}

#
print(f"Nome: {dicionario1['nome']}")

print("---------------------------------------------------------------------------------------")

# vai percorrer todo "dicionário", e depois exibir os dados
for chave, valor in dicionario1.items():
    
    # Exibi chave e o valor
    print(f"{chave} : {valor}")


print("")
print("================ 2. Remova um item de um dicionário e exiba o dicionário atualizado. =============")
print("")

# remover o a chave e seu valor, do dicionário "dicionario1"
del dicionario1 ["cidade"]


# Percorrer o "dicionario1",
for chave, valor in dicionario1.items():
    
    print(f"{chave} : {valor}")


print("")
print("================ 3. Crie um conjunto com cinco números e adicione um novo número. =============")
print("")

# Cria um conjunto, com vários números
conjunto_numeros = {1,2,3,4,5,6,7}

# Exibir conjunto que foi criado
print(f"Conjunto criado: {conjunto_numeros}") # saída => Conjunto criado: {1, 2, 3, 4, 5, 6, 7}

# Adiciona o número "24", dentro do conjunto
conjunto_numeros.add(24)

# Exibir conjunto atualizada
print(f"Conjunto atualizado: {conjunto_numeros}") # saída => Conjunto atualizado: {1, 2, 3, 4, 5, 6, 7, 24}


print("")
print("================ 4. Verifique se um valor existe dentro de um conjunto. =============")
print("")

# Conjunto de números pares
conjunto_pares = {2,4,6,8,10,12,14,16,18,20}

# Exibir conjunto criado
print(f"Conjunto pares: {conjunto_pares}") # saída => Conjunto pares: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print("")

# 
print("Verificando se no conjunto tem o número 4, se tiver retorna True, se não retorna False.")
print(4 in conjunto_pares) # saída => True


print("")
print("================ 5. Encontre a interseção entre dois conjuntos. =============")
print("")

# Criando uma união entre dois conjuntos
unidos = conjunto_numeros.union(conjunto_pares)

# Exibi o conjunto criado , unido
print(f"Conjuntos unidos: {unidos}")
# saída => Conjuntos unidos: {1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 24}


# vai separar do conjunto numeros, o conjunto pares e salvar na variável "insercao"
insercao = conjunto_pares.intersection(conjunto_numeros)


# Exibir na tela o resultado da separação, mostra o conjunto pares
print(f"Inserção dos conjuntos (separar os conjuntos): {insercao}") 
# saída => Inserção dos conjuntos (separar os conjuntos): {2, 4, 6}


print("")
print("================ 1. Crie um dicionário com três pares chave-valor e exiba um dos valores. =============")
print("")



