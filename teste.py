from grafo import Grafo

# Lê o grafo do arquivo "grafo_6.txt" e imprime a representação do grafo
# print(Grafo.le_grafo("grafo_6.txt"))

# Gera o arquivo "saida.txt" contendo informações sobre o grafo lido
# Grafo.le_grafo("grafo_6.txt").gera_arquivo()

# Gera uma lista de adjacência a partir do grafo lido e imprime sua 
# representação
# print(Grafo.le_grafo("grafo_6.txt").representa_grafo("lista"))

# Gera uma matriz de adjacência a partir do grafo lido e imprime sua
# representação
# print(Grafo.le_grafo("grafo_6.txt").representa_grafo("matriz"))

# Gera o arquivo "saida.txt" contendo informações (árvore de busca e níveis) 
# sobre a busca em largura realizada no grafo lido
# Grafo.le_grafo("grafo_6.txt").busca_grafo("bfs", "A")

# Gera o arquivo "saida.txt" contendo informações (árvore de busca e níveis) 
# sobre a busca em profundidade realizada no grafo lido
# Grafo.le_grafo("grafo_6.txt").busca_grafo("dfs")

# Gera o arquivo "saida.txt" contendo informações sobre componentes conexas 
# descobertas no grafo lido
# Grafo.le_grafo("grafo_8.txt").descobre_componentes_conexas()

# Calcula e imprime a distância entre um vértice e todos os outros de um grafo 
# não ponderado
print(Grafo.le_grafo("grafo_7.txt").calcula_distancia("G"))

# Calcula e imprime a distância entre um vértice e outro de um grafo não
# ponderado
# print(Grafo.le_grafo("grafo_7.txt").calcula_distancia("G", "D"))