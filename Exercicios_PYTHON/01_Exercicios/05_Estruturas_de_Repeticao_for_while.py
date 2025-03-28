#       5. Estruturas de Repetição (for/while)

print("===================================== Exercício 1 ============================================")
#   Exercício 16: Imprima os números de 1 a 10 usando um loop for.

# Usando o "range()", para gerar número, que inicia com 1 e vai até 10, está 11 por que começa a contar do 0
for i in range(1,11):
    
    # Vai exbir na tela, o número "i"
    print(f"Número: {i}")


print("===================================== Exercício 2 ============================================")
#   Exercício 17: Peça um número e exiba sua tabuada de 1 a 10.

# Pede ao usuário para adicionar um número
num1 = 5 # int(input("Digite um número:")) travado não pede ao usuário

# Vai gerar número de 1 a 10, e depois multiplica pelo número que o usuário adicionou
for n in range(1,11):
    
    print(f" {num1} * {n} = {num1 * n} " )
    
    

print("===================================== Exercício 3 ============================================")
#   Exercício 18: Some os números de 1 a 100 usando um loop for.

#   Variável "soma" que recebe o valor de 0
soma = 0

# Vai gerar números de 1 a 100, 
for r in range(1,101):
    
    # Cada vez que for gerador, vao somar e salva na variável "soma"
    soma += r
    
# Exibirá na tela o valor total da soma 
print(f"Somando os números de 1 a 100 é {soma}")



print("===================================== Exercício 4 ============================================")
#   Exercício 19: Continue pedindo números ao usuário até que ele digite um número negativo.



# Deixando o while repetindo sem para, por que está "True"
while True: 
    
    # Pedir ao usuário para adicionar um número
    num2 =  -1   # float(input("Digite um número:")) travado 
    
    # Se o valor for menor que zero, excuta a ação abaixo 
    if num2 < 0:
        
        print("Encerrando o loop!")
        
        # Para parar o while de funcionar "break"
        break



print("===================================== Exercício 5 ============================================")
#   Exercício 20: Peça ao usuário um número e verifique se ele é primo.

# Pede ao usuário para adicionar um número, e converte ele para inteiro
num3 = int(input("Digite um número:"))

# Se for maior que 1, já pode ser número primo, mas vai fazer outras verificações...
if num3 > 1:
    
    # Vai percorre os numeros de 2, ate o valor adicionado, -1,....
    for i in range(2,num3):
        
        # Se for divido por ele mesmo e o resto for 0, não é primo
        if num3 % i == 0:
            
            # Exibi na tela essa mensagem, com o número adicionado
            print(f"O número {num3} não é um número primo!")
            
            # Para parar o código 
            break
    else:
        #    
        print(f"O número {num3} é um número primo!")
        
else:
    # Números menores ou igual a 1, não são números primos
    print(f"O número {num3} não é um número primo!")
    
    
print("================================================ FIM =============================================")