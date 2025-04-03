
# Importa da pasta "meu_pacote", o modulo1.py
from meu_pacote import modulo1

# passa os valores para a função, que está no modulo1, e salva na var "resultadoSoma"
resultadoSoma = modulo1.soma(23,12)

# Exibi na tela
print(f"Resultado da soma: {resultadoSoma}") # saída => Resultado da soma: 35

# Importa da pasta "meu_pacote", o modulo 2
from meu_pacote import modulo2

# passa os valores para a função, que está no modulo2, e salva na var "resultadoMulti"
resultadoMulti = modulo2.multiplicar(5,5) # saída => Resultado da multiplicação: 25

# Exibi na tela
print(f"Resultado da multiplicação: {resultadoMulti}")