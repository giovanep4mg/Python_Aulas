####    Funções e Retorno de Valores

# 1. Escreva uma função que receba dois números e retorne a soma.
print("")
print("============================== 1. Escreva uma função que receba dois números e retorne a soma. ==========================")
print("")

# funçao que recebe dois números
def soma(a,b):
    
    # Faz a soma dos números e retorna o resultado da soma
    return a + b

# Executa a função, passando os valores de A e B, e salva o resultado na var "resultadoSoma"
resultaSoma = soma(2,3)

# Exibi na tela o resultado
print("Resultado da função soma: ",resultaSoma) # saída => Resultado da função soma:  5

print("")
print("============================== 2. Crie uma função que retorne o quadrado de um número. ==========================")
print("")

# Função que recebe um número...
def quadrado(numero):
    
    # Faz o cálculo e retorna o resultado
    return numero * numero

# A variável recebe o valor que será feito o cálculo
numero_add = 2

# Executa a função, passando o valor e exibirá na tela
print(f"O quadrado do número {numero_add} é {quadrado(numero_add)}") # saída => O quadrado do número 2 é 4


print("")
print("============================== 3. Escreva uma função que receba um nome e retorne uma saudação personalizada. ==========================")
print("")

# Funçao, que vai receber um nome e ....
def saudação(nome):
    
    # Exibirá essa mensagem com o nome adicionado
    print(f"Bem vindo, {nome}")


# Variável que guarda o nome
nome_add = "Giovani"

# Executa a função passando o nome que está dentro da variável
saudação(nome_add)

# Executa a função e passa o nome aqui mesmo na hora de chamar ela
saudação("Marcos")


print("")
print("============================== 4. Crie uma função que receba uma lista de números e retorne a média. ==========================")
print("")

#
def media(numeros):
    
    # Soma todos os números da lista
    soma = sum(numeros)
    
    # Divide pelo total de elementos da lista números
    result = soma / len(numeros)
    
    # Vai retorna o resultado da média
    return result
    
    
# Lista criada com vários números
numeros = [1,2,3,4,5,6]

# Exibi na tela o resultado 
print(f"A média é {media(numeros)}")



print("")
print("============================== 5. Faça uma função que verifique se um número é primo. ==========================")
print("")


# Função para verificar se o número é primo ou não
def primo(numero1):
    
    # Se o valor for maior que 1,...
    if numero1 > 1:
        
        # Percorre os números de 2 até "numero1" -1
        for i in range(2, numero1):
            
            # Verifica se ele tem divisor
            if numero1 % i == 0:
                # Se encontrar umm divisor não é primo, e exibi a mensagem
                print(f"O número {numero1} não é um número primo.")
                
                # Sai da função e retorna o resultado
                return
        
        # Se o loop terminou sem encontrar divisores, é primo    
        print(f"O número {numero1} é um número primo!")
                
    else:
        # Se o número for menor ou igual a 1
        print(f"O número {numero1} não é um número primo.")    
        
        
# Chama a função, passa o valor 
primo(11)
primo(7)
primo(4)
primo(1)


print("")
print("============================================= FIM ================================================")
print("")