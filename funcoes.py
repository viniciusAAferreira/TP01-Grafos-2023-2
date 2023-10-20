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
    excentricidades = []

    for outro_vertice in grafo.nodes():
        if outro_vertice != vertice:
            try:
                excentricidade = nx.shortest_path_length(grafo, source=vertice, target=outro_vertice)
                excentricidades.append(excentricidade)
            except nx.NetworkXNoPath:
                # Se não houver caminho entre os vértices, a excentricidade é infinita
                excentricidades.append(float('inf'))

    return max(excentricidades)

def determinar_raio_do_grafo(grafo):
    componentes_conectadas = list(nx.connected_components(grafo))
    menor_raio = float('inf')  # Inicializa com infinito para encontrar o mínimo

    for componente in componentes_conectadas:
        subgrafo = grafo.subgraph(componente)
        raio_componente = nx.radius(subgrafo)
        menor_raio = min(menor_raio, raio_componente)

    return menor_raio

def determinar_diametro_do_grafo(grafo):
    if not nx.is_connected(grafo):
        componentes_conectadas = list(nx.connected_components(grafo))
        diametros = []

        for componente in componentes_conectadas:
            subgrafo = grafo.subgraph(componente)
            if len(subgrafo) > 1:
                diametro_componente = nx.diameter(subgrafo)
                diametros.append(diametro_componente)

        if diametros:
            return max(diametros)
        else:
            return 0
    else:
        return nx.diameter(grafo)

def determinar_centro_do_grafo(grafo):
    if not nx.is_connected(grafo):
        componentes_conectadas = list(nx.connected_components(grafo))
        print(componentes_conectadas)
        menor_excentricidade = float('+inf')
        centro = set()

        for componente in componentes_conectadas:
            subgrafo = grafo.subgraph(componente)
            excentricidade = nx.eccentricity(subgrafo)
            menor_excentricidade_componente = min(excentricidade.values())

            if menor_excentricidade_componente < menor_excentricidade:
                menor_excentricidade = menor_excentricidade_componente
                centro = set(vertice for vertice in excentricidade if excentricidade[vertice] == menor_excentricidade)

        return centro
    else:
        excentricidade = nx.eccentricity(grafo)
        raio = min(excentricidade.values())
        return {vertice for vertice, excentricidade in excentricidade.items() if excentricidade == raio}


def determinar_sequencia_de_vertices_visitados_na_busca_em_largura(grafo, vertice):
    arvore_busca = nx.Graph()
    fila = [vertice]
    visitados = set()
    sequencia_vertices = []  # Para armazenar a sequência de vértices visitados

    while fila:
        vertice_atual = fila.pop(0)
        visitados.add(vertice_atual)
        sequencia_vertices.append(vertice_atual)  # Adiciona o vértice atual à sequência

        for vizinho in grafo.neighbors(vertice_atual):
            if vizinho not in visitados:
                fila.append(vizinho)
                arvore_busca.add_edge(vertice_atual, vizinho)

    arestas_nao_arvore = list(set(grafo.edges()) - set(arvore_busca.edges()))
    return sequencia_vertices, arestas_nao_arvore, arvore_busca

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




