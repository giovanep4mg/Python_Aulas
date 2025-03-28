###       3. Operadores Matemáticos

print("===================================== Exercício 1 ========================================")
#   Exercício 7: Peça três números ao usuário e calcule a média deles.

# Pegar os números do usuário
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

# Calcular a média dos números
media =  ( num1 + num2 + num3 ) / 3

# Exibir na tela o resultado da média dos números
print(f"A média é {media}")


print("===================================== Exercício 2 ========================================")
#   Exercício 8: Calcule a área de um círculo com base no raio fornecido pelo usuário.

# Pega o raio fornecido pelo usuário
a = float(input("Digite o raio do circulo:"))


# Calcular a área do circulo
resultado = 3.14 * (a) ** 2

# Exibir na tela o resultado
print("Resultado da área do circulo: ",resultado)


print("===================================== Exercício 3 ========================================")
#   Exercício 9: Converta um valor de reais para dólares com base na cotação informada.

#
valorReal = 100.00

# Converter (dividir o valor total => pelo valor de 1 dolar)
convertido = valorReal / 5.74

# Exibir o resultado
print(f"O valor de {valorReal} convertido para dolar fica {convertido}")


print("===================================== Exercício 4 ========================================")
#   Exercício 10: Peça um número e informe se ele é par ou ímpar.

# Pede ao usuário para adicionar um número
num4 = int(input("Digite um número:"))

# Usando o " % " retorna o resto da divisão
# Se o "num4" que é dividido por 2, e retorna o resto e se o resto for igual a 0
if num4 % 2 == 0:
    print(f"O número {num4} é par!")
else:
    print(f"O número {num4} é impar!")

print("===================================== fim ========================================")