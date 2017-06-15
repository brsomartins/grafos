def le_grafo(arquivo):
    """Entrada.

    A biblioteca deve ser capaz de ler um grafo a partir de um arquivo texto. 
    O formato do grafo no arquivo será o seguinte. A primeira linha informa o 
    número de vértices do grafo. Cada linha subsequente informa as arestas. Um 
    exemplo de um grafo e seu respectivo arquivo texto é dado na figura 1.
    """
    arquivo_aberto = open(arquivo, 'r')
    texto = arquivo_aberto.read()
    arquivo_aberto.close()
    linhas = texto.splitlines()
    quantidade_vertices = linhas[0]
    arestas = []

    for linha in linhas[1:]:
        linha_dividida = linha.split()

        if len(linha_dividida) == 2: # sem peso
            aresta = (linha_dividida[0], linha_dividida[1])
            arestas.append(aresta)
        elif len(linha_dividida) == 3: # com peso
            aresta = (linha_dividida[0], linha_dividida[1])
            peso = linha_dividida[2]
            arestas.append((aresta, peso))

    grafo = (quantidade_vertices, arestas)
    return(grafo)

def gera_arquivo(grafo):
    """Saída.
    
    Sua biblioteca deve ser capaz de gerar um arquivo texto com as seguintes 
    informações sobre o grafo: número de vértices, número de arestas e grau 
    médio, e distribuição empírica do grau dos vértices. A Figura 1 ilustra o 
    formato deste arquivo de saída para o grafo correspondente.
    """
    pass

def representa_grafo(grafo, estrutura = 'lista'):
    """Representação de grafos.

    Sua biblioteca deve ser capaz de representar grafos utilizando tanto uma 
    matriz de adjacência, quanto uma lista de adjacência. O usuário da 
    biblioteca (programa que irá usá-la) poderá escolher a representação a ser 
    utilizada.
    """
    pass

def busca_grafo(grafo, busca = 'bfs', raiz = None):
    """Busca em grafos: largura e profundidade.

    Sua biblioteca deve ser capaz de percorrer o grafo utilizando busca em 
    largura e busca em profundidade. O vértice inicial será dado pelo usuário 
    da biblioteca. A respectiva árvore de busca deve ser gerada assim como o 
    nível de cada vértice na árvore (nível da raiz é zero). Estas informações 
    devem ser impressas em um arquivo. Para descrever a árvore gerada, basta 
    informar o pai de cada vértice e seu nível no arquivo de saída. 
    """
    pass

def descobre_componentes_conexos(grafo):
    """Componentes conexos.

    Sua biblioteca deve ser capaz descobrir os componentes conexos de um 
    grafo. O número de componentes conexas, assim como o tamanho (em vértices) 
    de cada componente e a lista de vértices pertencentes à componente. Os 
    componentes devem estar listados em ordem decrescente de tamanho (listar 
    primeiro o componente com o maior número de vértices, etc).
    """
    pass

# print(le_grafo('grafo_5.txt'))