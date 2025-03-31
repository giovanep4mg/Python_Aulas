######    Métodos Úteis para Strings

#  Transformação de Maiúsculas e Minúsculas
print("============================== Transformação de Maiúsculas e Minúsculas ============================")
print("")


# Variável "texto1" recebe o texto => 
texto1 = "Python é incrível!"

print("Texto original: ",texto1) # Texto original:  Python é incrível!

# Usando o "upper()" deixa todo o texto em letras maiúscula.
print("Usando o upper(), deixamos todo texto assim: \n ",texto1.upper()) # PYTHON É INCRÍVEL!

# Usando o "lower()" deixamos todo o texto em letras minúscula
print("Usando o lower(), deixamos todo texto assim: \n",texto1.lower()) # python é incrível!

# Usando o "title()", deixamos em letra maiúscula primeira letra de cada palavra
print("Usando o title(), deixamos o texto assin: \n", texto1.title()) # Python É Incrível


print("")
print("==================================== Remoção de Espaços ============================================")
print("")


# A variável, recebe essa mensagem, com espaços nela
mensagem = "  Olá, mundo!  "

# Exibirá a mensagem, com espaço no inicio dela.
print("Mensagem original:",mensagem) # Mensagem original:  " Olá, mundo! "

# Exibirá a mensagem, atualizada, sem espaço
print("Mensagem atualizada:",mensagem.strip()) # Mensagem atualizada: "Olá, mundo!"

# Exibirá a mensagem, atualizada, deixa um espaço no final
print("Mensagem atualizada:",mensagem.lstrip()) # Mensagem atualizada: "Olá, mundo! "

# Exibirá a mensagem, atualizada, deixa um espaço no inicio do texto
print("Mensagem atualizada:",mensagem.rstrip()) # Mensagem atualizada: " Olá, mundo!"


print("")
print("==================================== Substituição de Caracteres ============================================")
print("")

# a variável "frase" recebe esse texto => "Eu gosto de java"
frase = "Eu gosto de java!"

# Exibi a frase que está dentro da variável
print("Frase atual: ",frase) # Frase atual:  Eu gosto de java!

# Vai modificar o texto antigo => "Java" pelo novo texto => "Python"
nova_frase = frase.replace("Java", "Python")

# Exibirá o texto atualizado, modificado com as frases trocadas
print("Frase nova: ",nova_frase) # Frase nova:  Eu gosto de java!



print("")
print("==================================== Quebra de Strings ============================================")
print("")

# Podemos dividir uma string em uma lista de palavras usando o método split().


# var guarda a frase
texto2 = "Aprender Python é divertido!"

# Usando o "split()", dividi a frase e torna ela uma lista, salva na var "palavras"
palavras = texto2.split()

# Exibirá a lista que foi criada, com as palavras separadas
print("Lista com as palavras separada: ",palavras) 
# Lista com as palavras separada:  ['Aprender', 'Python', 'é', 'divertido!']



print("")
print("==================================== Junção de Strings ============================================")
print("")

# Podemos juntar elementos de uma lista em uma única string usando join().

# Cria uma lista com palavras diferentes
palavras2 = ["Python","é","legal"]

# Usando o ".join()", juntamos as palavras da lista e salvamos no frase2
frase2 = " ".join(palavras2)

#
print("Texto juntado:",frase2) # Texto juntado: Python é legal



#####        Conclusão

# A manipulação de strings é uma habilidade essencial em Python. 
# Com essas técnicas, podemos trabalhar eficientemente com textos, 
# processar entradas de usuários e modificar conteúdos dinamicamente.

print("")
print("=======================================  FIM  ============================================")
print("")
