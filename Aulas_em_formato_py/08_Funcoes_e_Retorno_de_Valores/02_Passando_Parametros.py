#####     Passando Parâmetros

print("========================================================================================================")
print("")
#  Podemos passar valores para uma função através de parâmetros.

# Cria uma função, que vai receber como parâmetro "nome"
def cumprimentar(nome):
    
    # Exibirá na tela, essa mensagem, com o valor que foi adicionado no "nome"
    print(f"Olá {nome}")
    
# Chama a função, passando o valor do parâmetro => "Pedro"
cumprimentar("Pedro")   # saída => Olá Pedro

print("")
print("========================================================================================================")
print("")


def carro(nome_Carro):
    
    print(f"Seu carro é {nome_Carro}")
    
carro("gol") # saída => Seu carro é gol


print("")
print("========================================================================================================")
print("")

def idade(idade):
    
    print(f"Sua idade é {idade}")
    
idade("10") # saída => Sua idade é 10

print("")
print("========================================================================================================")
print("")