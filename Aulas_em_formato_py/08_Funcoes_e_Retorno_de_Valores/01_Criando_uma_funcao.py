#######          O que são Funções?

#   Funções são blocos de código reutilizáveis que executam uma tarefa específica. 
#   Elas ajudam a organizar o código e evitam repetições.

print("")
print("===============================Definição de uma Função   =====================================")
print("")

### Definição de uma função

# cria uma função com o nome "saudacao",...
def saudacao():
    
    # Exibirá na tela esse texto 
    print("Olá seja bem vindo!")

    
# Chama/executa a função "saudacao"
saudacao() # saída => Olá seja bem vindo!

print("")
print("================================= Funçao bomDia =============================================")
print("")


def bomDia():
    print("Bom dia!!")
    
# chama a funcao
bomDia() # saída => Bom dia!!

print("")
print("============================== Função Que interage com usuário  ==============================")
print("")


def nome():
    # Pede ao usuário para digitar um nome e salva na var "nome"
    nome = "nego" # str(input("Digite seu nome:")) travado
    
    # Exibirá na tela esse texto com o nome que o usuário digitou
    print(f"Olá {nome}")
    
    
# chama a função
nome() # saída => Olá nego


print("")
print("============================================== FIM =============================================")
print("")

