class Grafo:
    """Grafo"""
    def __init__(self, quantidade_vertices, arestas):
        self.quantidade_vertices = quantidade_vertices
        self.arestas = arestas

    def __str__(self):
        return "Grafo\nQuantidade de vértices: {}\nArestas: {}".format(self.
            quantidade_vertices, self.arestas)

    @staticmethod
    def le_grafo(arquivo):
        """Entrada.

        A biblioteca deve ser capaz de ler um grafo a partir de um arquivo 
        texto. O formato do grafo no arquivo será o seguinte. A primeira linha 
        informa o número de vértices do grafo. Cada linha subsequente informa 
        as arestas. Um exemplo de um grafo e seu respectivo arquivo texto é 
        dado na figura 1.
        """
        arquivo_aberto = open(arquivo, "r")
        texto = arquivo_aberto.read()
        arquivo_aberto.close()
        linhas = texto.splitlines()
        quantidade_vertices = int(linhas[0])
        arestas = {}

        for linha in linhas[1:]:
            linha_dividida = linha.split()

            if len(linha_dividida) == 2: # sem peso
                aresta = (linha_dividida[0], linha_dividida[1])
                arestas[aresta] = 1
            elif len(linha_dividida) == 3: # com peso
                aresta = (linha_dividida[0], linha_dividida[1])
                peso = linha_dividida[2]
                arestas[aresta] = peso

        grafo = Grafo(quantidade_vertices, arestas)
        return(grafo)

    def gera_arquivo(self):
        """Saída.
        
        Sua biblioteca deve ser capaz de gerar um arquivo texto com as 
        seguintes informações sobre o grafo: número de vértices, número de 
        arestas e grau médio, e distribuição empírica do grau dos vértices. A 
        Figura 1 ilustra o formato deste arquivo de saída para o grafo 
        correspondente.
        """
        arquivo = open("saida.txt", "w")
        arquivo.write("# n = {}".format(self.quantidade_vertices))
        arquivo.write("\n# m = {}".format(len(self.arestas)))
        arquivo.write("\n# d_medio = {}".format(2 * len(self.arestas) / self.
            quantidade_vertices))
        vertices = {}

        for aresta in self.arestas:
            for vertice in aresta:
                if vertice not in vertices:
                    vertices[vertice] = 1
                else:
                    vertices[vertice] += 1

        grau_maximo = 0

        for vertice in vertices:
            if vertices[vertice] > grau_maximo:
                grau_maximo = vertices[vertice]

        graus = {}
        total_graus = 0

        for grau in range(1, grau_maximo + 1):
            contador = 0

            for vertice in vertices:
                if vertices[vertice] == grau:
                    contador += 1
                    total_graus += 1

            graus[grau] = contador

        for grau in range(1, grau_maximo + 1):
            arquivo.write("\n{} {}".format(grau, graus[grau] / total_graus))

        arquivo.close()

    def representa_grafo(self, estrutura = "lista"):
        """Representação de grafos.

        Sua biblioteca deve ser capaz de representar grafos utilizando tanto 
        uma matriz de adjacência, quanto uma lista de adjacência. O usuário da 
        biblioteca (programa que irá usá-la) poderá escolher a representação a 
        ser utilizada.
        """
        if estrutura == "lista":
            grafo = {}
            
            for aresta in self.arestas:
                if aresta[0] in grafo.keys():
                    grafo[aresta[0]].update({aresta[1]: float(self.arestas[aresta])})
                else:
                    grafo[aresta[0]] = {aresta[1]: float(self.arestas[aresta])}

                if aresta[1] in grafo.keys():
                    grafo[aresta[1]].update({aresta[0]: float(self.arestas[aresta])})
                else:
                    grafo[aresta[1]] = {aresta[0]: float(self.arestas[aresta])}
        elif estrutura == "matriz":
            grafo = [[]]

            # for aresta in self.arestas:

        # print(self.arestas)

        return(grafo)

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

# print(Grafo.le_grafo('grafo_5.txt'))
# Grafo.le_grafo('grafo_2.txt').gera_arquivo()
# print(Grafo.le_grafo('grafo_5.txt').representa_grafo())
print(Grafo.le_grafo('grafo_0.txt').representa_grafo("matriz"))