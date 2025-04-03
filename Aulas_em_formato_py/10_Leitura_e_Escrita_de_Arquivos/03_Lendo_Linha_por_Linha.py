#####           Lendo Linha por Linha

#
arquivo = open(r"C:\Users\giova\OneDrive\Área de Trabalho\Python_Aulas\Aulas_em_formato_py\10_Leitura_e_Escrita_de_Arquivos\exemplo.txt", "r")

#
for linha in arquivo:
    
    #
    print(linha.strip()) # "strip()" => remove quebras de linhas extras
    
#
arquivo.close()