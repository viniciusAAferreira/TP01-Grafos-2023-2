import networkx as nx

def calcular_ordem_do_grafo_graphml(grafo):
    return grafo.number_of_nodes()

def calcular_tamanho_do_grafo(grafo):
    return grafo.number_of_edges()

def encontrar_vizinhos_do_vertice(grafo, vertice):
    vizinhos = list(grafo.neighbors(vertice))
    return vizinhos

def determinar_grau_do_vertice(grafo, vertice):
    grau = grafo.degree(vertice)
    return grau

def calcular_sequencia_de_graus(grafo):
    sequencia_de_graus = list(grafo.degree())
    return sequencia_de_graus

def determinar_excentricidade_do_vertice(grafo, vertice):
    excentricidades = nx.single_source_shortest_path_length(grafo, source=vertice)
    excentricidade = max(excentricidades.values())
    return excentricidade

def determinar_raio_do_grafo(grafo):
    raio = nx.radius(grafo)
    return raio

def determinar_diametro_do_grafo(grafo):
    diametro_do_grafo = nx.diameter(grafo)
    return diametro_do_grafo

def determinar_centro_do_grafo(grafo):
    centro_do_grafo = nx.center(grafo)
    return centro_do_grafo


def busca_em_largura_com_arvore(grafo, vertice_inicial):
    arvore_busca = nx.Graph()
    fila = [vertice_inicial]
    visitados = set(fila)
    sequencia_vertices = []  # Para armazenar a sequência de vértices visitados

    while fila:
        vertice_atual = fila.pop(0)
        sequencia_vertices.append(vertice_atual)  # Adiciona o vértice atual à sequência

        for vizinho in grafo.neighbors(vertice_atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                arvore_busca.add_edge(vertice_atual, vizinho)

    # Arestas que não fazem parte da árvore de busca em largura
    arestas_nao_arvore = list(set(grafo.edges()) - set(arvore_busca.edges()))

    return arvore_busca, arestas_nao_arvore, sequencia_vertices

def determinar_distancia_entre_dois_vertices(grafo, vertice_origem, vertice_destino):
    distancia = nx.shortest_path_length(grafo, source=vertice_origem, target=vertice_destino)
    
    caminho_minimo = nx.shortest_path(grafo, source=vertice_origem, target=vertice_destino)

    return distancia, caminho_minimo

def calcular_centralidade_de_proximidade(grafo, vertice):
    distancias = nx.single_source_shortest_path_length(grafo, vertice)
    soma_distancias = sum(distancias.values())
    numero_de_vertices = grafo.number_of_nodes()
    centralidade_de_proximidade = (numero_de_vertices - 1) / soma_distancias
    return centralidade_de_proximidade




