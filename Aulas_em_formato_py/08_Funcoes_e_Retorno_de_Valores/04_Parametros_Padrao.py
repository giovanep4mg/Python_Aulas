#####       Parâmetros Padrão

#  Podemos definir valores padrão para os parâmetros de uma função.

print("================ Podemos definir valores padrão para os parâmetros de uma função ==========================")
print("")

# A função, recebe 2 parâmetro, a base e o expoente, que já possui um valor, mas pode ser trocado
def potencia(base, expoente=2):
    
    # Irá fazer o cálculo e retornará o resultado
    return base ** expoente

print("Resultado da potencia, com parâmetro 3: ",potencia(3)) 
# saída => Resultado da potencia, com parâmetro 3:  9


print("--------------------------------------------------------------------------------------------")


print("Resultado da potencia, com parâmetro 2 , 3: ",potencia(2,3))
# Resultado da potencia, com parâmetro 2 , 3:  8

print("")
print("======================================================================================")
print("")

def calcular_desconto(valor, desconto=10):
    
    # Faz o cálculo e retornará o resultado
    return valor - (valor * desconto / 100)

print("Calcular o desconto, passando como parâmetro o valor de 100", calcular_desconto(100))
# Calcular o desconto, passando como parâmetro o valor de 100 90.0

print("--------------------------------------------------------------------------------------------")


print("Calcular o desconto, passando o valor e o valor do desconto: ",calcular_desconto(100, 30))
# Calcular o desconto, passando o valor e o valor do desconto:  70.0


print("")
print("======================================================================================")
print("")

def saudacao(nome, mensagem= "Bem vindo!"):
    
    # Vai retorna a mensagem, com o nome
    return f"{mensagem} {nome}!"


print("Executando a função: ",saudacao("pedro"))
# Executando a função:  Bem vindo! pedro

print("--------------------------------------------------------------------------------------------")

# passa os parâmetros, nome e uma mensagem diferente
print(saudacao("Marcos", "Me pague!"))

print("")
print("======================================================================================")
print("")

def criar_usuario(nome, idade=18,cidade="Rio"):
    return f"Nome: {nome}, idade: {idade}, cidade:{cidade}"

# Passando apenas o parâmetro "nome"
print(criar_usuario("Maria")) # Nome: Maria, idade: 18, cidade:Rio

print("--------------------------------------------------------------------------------------------")

# Passando os parâmetros => "nome", "idade" e "cidade", vai mudar tudo
print(criar_usuario("Paulo",32,"Passa-Quatro"))
# Nome: Paulo, idade: 32, cidade:Passa-Quatro




print("")
print("======================================================================================")
print("")