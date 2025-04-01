##########    Manipulação de Strings

print("")
print("========================== 1. Converta uma string para maiúsculas. =============================")
print("")

# A variável "texto1" vai receber esse texto e salva 
texto1 = "Olá como vai você, espero que esteja tudo bem!"

# Usando o "upper()" converte o texto para letras maiúscula e salva na variável "maiuscula"
maiusculas = texto1.upper()

# Exibi na tela
print(maiusculas) # saída => OLÁ COMO VAI VOCÊ, ESPERO QUE ESTEJA TUDO BEM!


print("")
print("========================== 2. Remova os espaços extras de uma string. =============================")
print("")


# Variável que vai receber esse texto com espaço
texto2 = "  Tudo bom?!  "

# Exibi o texto original, com espaço
print(f"Texto original:{texto2}") # saída => Texto original:  Tudo bom?!

# Usando o "strip()" para retirar os espaços do texto
sem_espaco = texto2.strip()

# Exibir na tela
print(f"Texto modificado:{sem_espaco}") # saída => Texto modificado:Tudo bom?!


print("")
print("================= 3. Substitua todas as ocorrências de uma palavra dentro de uma string. ==================")
print("")


# A variável "texto3" vai guarda esse texto
texto3 = "Meu nome é João Paulo, moro na cidade de Passa-Quatro!"

# Exibi na tela o texto original
print(f"Texto original:\n {texto3}")

# Usando o "replace()" Muda o nome "Passa-Quatro" para "Itanhandu", e salva na variável "texto3_modificado" 
texto3_modificado = texto3.replace("Passa-Quatro", "Itanhandu")

# Exibir na tela o texto atualizado
print(f"Texto modificado:\n {texto3_modificado}")


print("")
print("========================== 4. Inverta os caracteres de uma string. =============================")
print("")

# 
texto4 = "Python"

#
print(f"Texto: {texto4}") # saída => Texto: Python

# Usando o "[::-1]" para inverter o texto
texto_invertido = texto4[::-1]

#
print(f"Texto invertido: {texto_invertido}") # saída => Texto invertido: nohtyP


print("")
print("========================== 5. Verifique se uma string é um palíndromo. =============================")
print("")

# Função que vai receber um texto
def palindromo(texto5):
    
    # coloca o texto em letras minúsculas, tira os espaços e salva na variável "texto5"
    texto5 = texto5.replace(" "," ").lower()
    
    # Inverte o texto, depois compara se são iguais, retorna => True ou False
    return texto5 == texto5[::-1]


# Variáveis com palavras para testar 
palavra = "radar"
palavra2 = "Python"


# Exibi na tela, a palavra e se é ou não um palíndromo
print(f"A palavra '{palavra}' é palíndromo? {palindromo(palavra)}")
# saída => A palavra radar é palíndromo? True


#
print(f"A palavra '{palavra2}' é palíndromo? {palindromo(palavra2)}")
# saída => A palavra Python é palíndromo? False


print("")
print("==================================== FIM ============================================")
print("")

