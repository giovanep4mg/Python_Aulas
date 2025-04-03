####    01_Abrindo_um_Arquivo.py

#   Em Python, podemos ler e escrever arquivos usando a função open(). 
#   Isso permite armazenar e recuperar informações facilmente.


# Seleciona um arquivo, para leitura "r", salva na variável => arquivo
arquivo = open(r"C:\Users\giova\OneDrive\Área de Trabalho\Python_Aulas\Aulas_em_formato_py\10_Leitura_e_Escrita_de_Arquivos\exemplo.txt", "r")


# Lê o conteúdo do arquivo
conteudo = arquivo.read()

# Exibir conteúdo
print(conteudo)

# Fecha o arquivo
arquivo.close()


###        Modos de abertura:

#   "r": leitura
#   "w": escrita (sobrescreve o arquivo)
#   "a": escrita (adiciona ao final do arquivo)
#   "x": cria um novo arquivo


