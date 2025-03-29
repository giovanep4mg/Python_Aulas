#########         Funções com Múltiplos Retornos

##  Uma função pode retornar múltiplos valores.

print("============================================================================================")
print("")


def calcular_dobro_triplo(numero):
    
    # fará o cálculo de numero x 2, numero x 3, 3 retornará o resultado
    # na primeira posição, será dobrado o número, na segunda será triplicado o número
    return numero * 2, numero * 3


# passa o valor para a função "4", guarda nas variáveis o resultado
# a 1 var é que vai guarda o resultado de ( numero * 2 ) => dobro
# a 2 var é que vai guarda o resultado de ( numero * 3 ) => triplo
dobro, triplo = calcular_dobro_triplo(4)


# exibirá na tela, 
print("dobro => ",dobro)

print("triplo => ",triplo)