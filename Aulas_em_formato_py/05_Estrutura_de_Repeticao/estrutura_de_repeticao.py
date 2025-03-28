######   🔄 Estrutura de Repetição: for
## O laço for é utilizado para iterar sobre sequências (listas, strings, range, etc.).

print("====================================== Iterando sobre uma lista ===================================")
# Exemplo 1: Iterando sobre uma lista

# cria uma lista "nomes", que recebe esses nomes
nomes = ["Giovani","João","Paulo","Marcos"]

# Vai percorrer a lista "nomes", e a cada vez que isso acontecer, vai salvar um item na var "nome"
for nome in nomes:
    # Exibi na tela esse texto com o item, enquanto houver item dentro da lista
    print(f"Olá {nome}!")
    
    
print("====================================== Usando  range() ===================================")
# Exemplo 2: Usando range()

# range(5) → Gera uma sequência de números que começa em 0 e vai até 4 (o range(n) gera números de 0 até n-1).
#  O laço for percorre essa sequência, atribuindo cada valor a i a cada iteração.
for i in range(5):
    
    # Exibir na tela o valor da variável "i"
    print(i)
    

print("=====================================  Estrutura de Repetição: while  ===============================")
###  🔄 Estrutura de Repetição: while
#  O laço while executa um bloco de código enquanto uma condição for verdadeira.

# Exemplo 1: Contador simples

# Variável "contador" recebe o valor de 0
contador = 0

# Enquanto valor da var for menor que 5, vai...
while contador < 5:
    
    # Exibir na tela, texto e o valor que está na var "contador"
    print(f"Contador: {contador}")
    
    # Importante, adiciona mais 1 ao valor da var "contador", para parar o loop
    contador += 1
    
    
# Exemplo 2: Entrada do usuário

# var "resposta" não recebe nada, está vazia
resposta = ""

# Enquanto, o valor da var  não for igual a "sair", vai ficar executando esse código...
while resposta != "sair":
    
    # Pede ao usuário para digitar algo ou digitar sair
    resposta = input("Digite algo (ou 'sair' para encerrar): ")
    
    # Exibi na tela, o que o usuário adicionou
    print(f"Você digitou: {resposta}")
    
    
###         📌 Resumo
##      for é usado para iterar sobre sequências.
##      while executa enquanto a condição for verdadeira.
##      Para evitar loops infinitos, sempre garanta que a condição de parada seja atingida.