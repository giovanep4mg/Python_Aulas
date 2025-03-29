##############            Dicionários em Python
#  Um dicionário armazena pares chave-valor.

print("================================== Criando Dicionário =====================================================")
print("")
###     Criando um dicionário

#
dados = {
    "nome": "João",
    "idade": "32",
    "cidade": "Rio"
}

print("-------------------------------------------------------------------------------------------------------------")

#
contatos_lista = {
    "Pedro" : "35999999999",
    "Marcos" : "35999999999",
    "Maria" : "35999999999",
    "João" : "35999999999",
}


print(f"Dados do dicionário: {dados}") 
# Dados do dicionário: {'nome': 'João', 'idade': '32', 'cidade': 'Rio'}


print("-------------------------------------------------------------------------------------------------------------")


print(f"Dados do dicionário contato: {contatos_lista}")
# Dados do dicionário contato: {'Pedro': '35999999999', 'Marcos': '35999999999', 'Maria': '35999999999', 'João': '35999999999'}


print("")
print("================================== Acessando valores =====================================================")
print("")

print("Acessando os valores, do dicionário:", dados["nome"]) # Acessando os valores, do dicionário: João
print("Acessando os valores, do dicionário:", dados["idade"]) # Acessando os valores, do dicionário: 32
print("Acessando os valores, do dicionário:", dados["cidade"]) # Acessando os valores, do dicionário: Rio

print("-------------------------------------------------------------------------------------------------------------")


print("Acessando os valores do dicionário contato:", contatos_lista["Pedro"])
# Acessando os valores do dicionário contato: 35999999999

print("")
print("============================= Adicionando um novo par chave-valor  ===========================================")
print("")

# Inserir no dicionário => "dados", chave => "profissão" e o valor => "Engenheiro"
dados ["profissão"] = "Engenheiro"

print(f"Dados do dicionário, atualizado: {dados}") 
# Dados do dicionário, atualizado: {'nome': 'João', 'idade': '32', 'cidade': 'Rio', 'profissão': 'Engenheiro'}

print("-------------------------------------------------------------------------------------------------------------")


# Inserir no dicionário "contatos_lista", chave => "Luiza" e o valor => "9293929192"
contatos_lista ["Luiza"] = "9293929192"

print(f"Dados do dicionário, contato lista: {contatos_lista}")
# Dados do dicionário, contato lista: {'Pedro': '35999999999', 'Marcos': '35999999999', 'Maria': '35999999999', 'João': '35999999999', 'Luiza': '9293929192'}

print("")
print("================================== Alterando um valor  ===========================================")
print("")

# Inseri o valor => "31", na chave => "idade", dentro do dicionário => "dados"
dados ["idade"] = "31"

#
print(f"Dados do dicionário, alterando a idade: {dados}") 
# Dados do dicionário, alterando a idade: {'nome': 'João', 'idade': '31', 'cidade': 'Rio', 'profissão': 'Engenheiro'}

print("-------------------------------------------------------------------------------------------------------------")


# Inserir o valor "232121212", na chave "Maria", no dicionário contato_lista
contatos_lista ["Maria"] = "232121212"

#
print(f"Dados do dicionário, contato_lista, alterando o número de Maria: \n {contatos_lista}")
# Dados do dicionário, contato_lista, alterando o número de Maria:
# {'Pedro': '35999999999', 'Marcos': '35999999999', 'Maria': '232121212', 'João': '35999999999', 'Luiza': '9293929192'}


print("")
print("================================== Removendo um item  ===========================================")
print("")

# Pega a chave => "cidade", dentro do dicionário "dados", e remove/deleta "del"
del dados ["cidade"]


print(f"Dados do dicionário, removendo 'cidade': {dados}") 
# Dados do dicionário, removendo 'cidade': {'nome': 'João', 'idade': '31', 'profissão': 'Engenheiro'}


print("-------------------------------------------------------------------------------------------------------------")


# Pega a chave "Marcos", dentro do dicionário, e remove ele
del contatos_lista ["Marcos"]

#
print(f"Removendo do dicionário, contato_lista, o nome Marcos: {contatos_lista}")
# Removendo do dicionário, contato_lista, o nome Marcos: {'Pedro': '35999999999', 'Maria': '232121212', 'João': '35999999999', 'Luiza': '9293929192'}


print("")
print("================================== Iterando sobre um dicionário  ===========================================")
print("")


for chave, valor in dados.items():
    print(f"{chave} : {valor}")

# Vai exibir assim na tela:

#   nome : João
#   idade : 31
#   profissão : Engenheiro

print("-------------------------------------------------------------------------------------------------------------")


for chave, valor in contatos_lista.items():
    print(f"{chave} : {valor}")
    
# Vai exibir assim na tela:

# Pedro : 35999999999
# Maria : 232121212
# João : 35999999999
# Luiza : 9293929192
    
    

print("")
print("========================================== FIM ================================================")
print("")