######          Usando "with open"

with open(r"C:\Users\giova\OneDrive\Área de Trabalho\Python_Aulas\Aulas_em_formato_py\10_Leitura_e_Escrita_de_Arquivos\exemplo.txt", "r") as arquivo:
    
    conteudo = arquivo.read()
    
    print(conteudo)