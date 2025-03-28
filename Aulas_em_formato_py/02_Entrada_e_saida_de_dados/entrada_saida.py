# Para exibir informações na tela usamos o "print", exemplo:
print("OLá mundo!")

# Exibir números e expressões matemáticas
 
print(5 + 5 )

print("-------------------------------------------------------------------------------------")
#  Exibir variáveis
nome = "João"
idade = 29

print("Nome: ",nome)
print("Idade:",idade)

print("-------------------------------------------------------------------------------------")
# Usando f-strings para formatar saída

nome1 = "Ana Luiza"
idade1 = 23

print(f"Meu nome é {nome1}, eu tenho {idade1} anos de idade!")

print("-------------------------------------------------------------------------------------")

########## Entrada de dados ##########################
#  A função "input" permite pegar os dados do usuário

# Exemplo 1 => Pedindo um nome ao usuário
nomeUsuario = input("Digite um nome:")

# Exemplo 2 => Pedindo um número ao usuário
idadeUsuario = input("Digite sua idade:")

# Exemplo 3 => Convertendo a entrada para número
num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))

# Realizando o cálculo
soma = num1 + num2

# Exibindo o que o usuário digitou
print(f"Nome do usuário é {nomeUsuario} ")
print(f"A idade do usuário é {idadeUsuario}")
print(f"O valor da soma dos números digitados é {soma}")

######## Para realizar cálculos, converta para => int ou float