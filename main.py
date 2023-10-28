import networkx as nx
from funcoes import *
import matplotlib.pyplot as plt

# arquivo_graphml = "./Arquivos/exemplo_BuscaLargura_Slide.graphml"

# grafo = nx.read_graphml(arquivo_graphml)
# opcao = -1

# pos = nx.planar_layout(grafo)

arq = "./Arquivos/"
arquivo = input("Digite o nome do arquivo do grafo: ")
arquivo_graphml = arq + arquivo + '.graphml'

try:
    grafo = nx.read_graphml(arquivo_graphml)
    opcao = -1

    # Cria um layout para o grafo
    pos = nx.planar_layout(grafo)

except (IOError, FileNotFoundError) as e:
    print(f"Erro na leitura do arquivo: {e}")



nx.draw(grafo, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold')
edge_labels = nx.get_edge_attributes(grafo, "weight")
nx.draw_networkx_edge_labels(grafo, pos, edge_labels)

plt.title("Grafo Lido do Arquivo GraphML")
ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()

while opcao != 0:
    print("#############################################")
    print("1 - Calcular ordem do grafo")
    print("2 - Calcular tamanho do grafo")
    print("3 - Encontrar vizinhos do vértice")
    print("4 - Determinar grau do vértice")
    print("5 - Calcular sequência de graus")
    print("6 - Determinar excentricidade do vértice")
    print("7 - Determinar raio do grafo")
    print("8 - Determinar diâmetro do grafo")
    print("9 - Determinar centro do grafo")
    print("10 - Determinar sequência de vértices visitados na busca em largura")
    print("11 - Determinar distância e caminho mínimo")
    print("12 - Calcular centralidade de proximidade")
    print("0 - Sair")
    print("#############################################")
    

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        ordem_do_grafo = calcular_ordem_do_grafo_graphml(grafo)
        print("Ordem do grafo:", ordem_do_grafo)
        print("\n")

    elif opcao == 2:
        tamanho_do_grafo = calcular_tamanho_do_grafo(grafo)
        print("Tamanho do grafo:", tamanho_do_grafo)
        print("\n")

    elif opcao == 3:
        vertice_fornecido = input("Digite o vértice: ")
        vizinhos = encontrar_vizinhos_do_vertice(grafo, vertice_fornecido)
        print(f"Vizinhos do vértice {vertice_fornecido}: {vizinhos}")
        print("\n")

    elif opcao == 4:
        vertice_fornecido = input("Digite o vértice: ")
        grau_do_vertice = determinar_grau_do_vertice(grafo, vertice_fornecido)
        print(f"Grau do vértice {vertice_fornecido}: {grau_do_vertice}")
        print("\n")
    
    elif opcao == 5:
        sequencia_de_graus = calcular_sequencia_de_graus(grafo)
        print("Sequência de graus do grafo:", sequencia_de_graus)
        print("\n")
    
    elif opcao == 6:
        vertice_fornecido = input("Digite o vértice: ")
        excentricidade_do_vertice = determinar_excentricidade_do_vertice(grafo, vertice_fornecido)
        print(f"Excentricidade do vértice {vertice_fornecido}: {excentricidade_do_vertice}")
        print("\n")
    
    elif opcao == 7:
        raio_do_grafo = determinar_raio_do_grafo(grafo)
        print("Raio do grafo:", raio_do_grafo)
        print("\n")

    elif opcao == 8:
        diametro_do_grafo = determinar_diametro_do_grafo(grafo)
        print("Diâmetro do grafo:", diametro_do_grafo)
        print("\n")
    
    elif opcao == 9:
        centro_do_grafo = determinar_centro_do_grafo(grafo)
        print("Centro do grafo:", centro_do_grafo)
        print("\n")
    
    elif opcao == 10:
        vertice_inicial = input("Digite o vértice inicial: ")
        arvore_busca, arestas_nao_arvore, sequencia_vertices = busca_em_largura_com_arvore(grafo, vertice_inicial)
        
        print("Sequência de vértices visitados na busca em largura:", sequencia_vertices)
        print("Arestas que não fazem parte da árvore de busca em largura:", arestas_nao_arvore)
        nx.write_graphml(arvore_busca, "arvore_busca.graphml")
        
        criaLayout = input("Deseja criar um layout para a árvore de busca? (S/N) ")
        
        if criaLayout == "S" or criaLayout == "s":
            grafo_Busca = nx.read_graphml("arvore_busca.graphml")
            p = nx.planar_layout(grafo)

            nx.draw(grafo_Busca, p, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold')
            plt.title("Grafo Busca Largura")
            plt.axis('on')
            plt.show()
        print("\n")

    elif opcao == 11:
        vertice_origem = input("Digite o vértice de origem: ")
        vertice_destino = input("Digite o vértice de destino: ")
        distancia, caminho_minimo = determinar_distancia_entre_dois_vertices(grafo, vertice_origem, vertice_destino)
        print(f"Distância entre os vértices {vertice_origem} e {vertice_destino}: {distancia}\n E o caminho mínimo é: {caminho_minimo}")
        print("\n")

    elif opcao == 12:
        vertice_fornecido = input("Digite o vértice: ")
        centralidade_de_proximidade = calcular_centralidade_de_proximidade(grafo, vertice_fornecido)
        print(f"Centralidade de proximidade do vértice {vertice_fornecido}: {centralidade_de_proximidade}")
        print("\n")

    elif opcao == 0:
        print("\n")
        print("Saindo do programa...")

    else:
        print("Opção inválida. Por favor, tente novamente.")
        print("\n")