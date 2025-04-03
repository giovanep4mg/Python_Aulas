#######     Escrevendo em Arquivos

# Abre o arquivo para leitura "r", e salva na variável "arquivo"
arquivo = open(r"C:\Users\giova\OneDrive\Área de Trabalho\Python_Aulas\Aulas_em_formato_py\10_Leitura_e_Escrita_de_Arquivos\exemplo.txt", "w")

# escreve um novo arquivo
arquivo.write('Olá mundo!\n')

# escreve um novo arquivo
arquivo.write('Testando escrever no bloco de notas!\n')

arquivo.write("Escrevendo uma nova linha no exemplo.txt\n")

# escreve um novo arquivo
arquivo.write('Eu sei, na verdade não sei o que colocar aqui!\n')

arquivo.write("Testando se adiciona o texto e se vai abrir depois.\n")

arquivo.close()

#######  Vai exibir o arquivo modificado

# Seleciona um arquivo, para leitura "r", salva na variável => arquivo
arquivo = open(r"C:\Users\giova\OneDrive\Área de Trabalho\Python_Aulas\Aulas_em_formato_py\10_Leitura_e_Escrita_de_Arquivos\exemplo.txt", "r")


# Lê o conteúdo do arquivo
conteudo = arquivo.read()

# Exibir conteúdo
print(conteudo)

# Fecha o arquivo
arquivo.close()