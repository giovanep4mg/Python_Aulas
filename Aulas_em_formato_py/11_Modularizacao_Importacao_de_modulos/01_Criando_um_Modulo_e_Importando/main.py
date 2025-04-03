
# Arquivo Principal

print("")
print("=============================== Importação Simples ================================================")
print("")

# Vai importa o modulo
import meu_modulo

# Passa o nome, para a função => "saudacao", que está no modulo => "meu_modulo", e exibi na tela
print(meu_modulo.saudacao("Giovani"))

 
print("")
print("======================== Importando um Item Específico ===========================================")
print("")

# Vai no modulo e importa a função "saudacao"
from meu_modulo import saudacao

# Passa o nome "Maria", para a função => saudacao, e exibi na tela
print(saudacao("Maria"))

print("")
print("================================= Importação com Alias ============================================")
print("")

# Importa o modulo e muda o nome do modulo para "mm"
import meu_modulo as mm 

# passa o nome, dentro da função => saudação que está no modulo => meu_modulo
print(mm.saudacao("Carlos"))


print("")
print("=================================== Importando Tudo =============================================")
print("")

# Importa tudo
from meu_modulo import*

# Passa o nome, na função => "saudacao" e exibi na tela
print(saudacao("Ana"))


print("")
print("===================================== Fim =======================================================")
print("")
