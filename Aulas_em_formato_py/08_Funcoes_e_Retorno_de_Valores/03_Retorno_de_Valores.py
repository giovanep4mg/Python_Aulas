#############    Retorno de Valores

#   Uma função pode retornar um valor usando a palavra-chave return.

print("====================================== Retorno de Valores ======================================")
print("")

# Cria uma função, que vai receber dois parâmetros "a" e "b"
def soma( a , b ):
    
    # Soma os valores de a + b, e retorna o resultado
    return a + b

# Passa os valores de "a => 5" e "b => 10", executa a função, o resultado será salvo na var "resultado"
resultado = soma(5,10)

# Exibirá na tela o resultado
print(f"O resultado da soma é {resultado}") # saída => O resultado da soma é 15

print("")
print("====================================================================================================================")
print("")

def subtracao(s,d):
    return s - d

resultado_Sub = subtracao(8,4)
print(f"Resultada da funcao subtracao: {resultado_Sub}") # saída => Resultada da funcao subtracao: 4


print("")
print("====================================================================================================================")
print("")