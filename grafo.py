def leGrafo(arquivo):
	"""Entrada.

	A biblioteca deve ser capaz de ler um grafo a partir de um 
	arquivo texto. O formato do grafo no arquivo será o seguinte. A 
	primeira linha informa o número de vértices do grafo. Cada linha 
	subsequente informa as arestas. Um exemplo de um grafo e seu 
	respectivo arquivo texto é dado na figura 1.
	"""
	pass

def geraArquivo(grafo):
	"""Saída.
	
	Sua biblioteca deve ser capaz de gerar um arquivo texto com as 
	seguintes informações sobre o grafo: número de vértices, número 
	de arestas e grau médio, e distribuição empírica do grau dos 
	vértices. A Figura 1 ilustra o formato deste arquivo de saída 
	para o grafo correspondente.
	"""
	pass

def representaGrafo(grafo, estrutura = 'lista'):
	"""Representação de grafos.

	Sua biblioteca deve ser capaz de representar grafos utilizando 
	tanto uma matriz de adjacência, quanto uma lista de adjacência. 
	O usuário da biblioteca (programa que irá usá-la) poderá 
	escolher a representação a ser utilizada.
	"""
	pass

def buscaGrafo(grafo, busca = 'bfs', raiz = None):
	"""Busca em grafos: largura e profundidade.

	Sua biblioteca deve ser capaz de percorrer o grafo utilizando 
	busca em largura e busca em profundidade. O vértice inicial será 
	dado pelo usuário da biblioteca. A respectiva árvore de busca 
	deve ser gerada assim como o nível de cada vértice na árvore 
	(nível da raiz é zero). Estas informações devem ser impressas em 
	um arquivo. Para descrever a árvore gerada, basta informar o pai 
	de cada vértice e seu nível no arquivo de saída. 
	"""
	pass

def descobreComponentesConexos(grafo):
	"""Componentes conexos.

	Sua biblioteca deve ser capaz descobrir os componentes conexos 
	de um grafo. O número de componentes conexas, assim como o 
	tamanho (em vértices) de cada componente e a lista de vértices 
	pertencentes à componente. Os componentes devem estar listados 
	em ordem decrescente de tamanho (listar primeiro o componente 
	com o maior número de vértices, etc).
	"""
	pass