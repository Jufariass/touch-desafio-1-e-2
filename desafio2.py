import os
import heapq

def ler_entrada2():
    try:
        caminho_arquivo = os.path.join(os.getcwd(), "entrada2.txt")
        with open(caminho_arquivo, "r") as f:
            linhas = f.readlines()

        print("Arquivo teve sucesso!") 
        print("Linhas do arquivo:", linhas)  

        cidades = {}
        adjacencias = {}

        # Processa as cidades e as adjacências
        i = 0
        while linhas[i].strip() != '--':
            cidade, cep_inicial, cep_final = linhas[i].strip().split(",")
            cidades[cidade] = (int(cep_inicial), int(cep_final))
            i += 1

        print("Cidades lidas:", cidades)

        
        i += 1
        while i < len(linhas) and linhas[i].strip() != '--':
            cidade1, cidade2, custo = linhas[i].strip().split(",")
            custo = float(custo)
            if cidade1 not in adjacencias:
                adjacencias[cidade1] = []  # A chave agora é a cidade
            if cidade2 not in adjacencias:
                adjacencias[cidade2] = []  # A chave agora é a cidade
            adjacencias[cidade1].append((cidade2, custo))
            adjacencias[cidade2].append((cidade1, custo))
            i += 1

        print("Adjacências lidas:", adjacencias)

        # Último CEP
        cidade_origem, cidade_destino = linhas[i + 1].strip().split(",")
        print("Cidade origem:", cidade_origem)
        print("Cidade destino:", cidade_destino)
        return cidade_origem.strip(), cidade_destino.strip(), adjacencias

    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None, None, None

def dijkstra(adjacencias, origem, destino):
    if origem not in adjacencias:
        print(f"Erro: A cidade de origem {origem} não existe nas adjacências.")
        return None
    if destino not in adjacencias:
        print(f"Erro: A cidade de destino {destino} não existe nas adjacências.")
        return None

    dist = {cidade: float('inf') for cidade in adjacencias}
    dist[origem] = 0
    pq = [(0, origem)]

    while pq:
        current_dist, current_cidade = heapq.heappop(pq)

        if current_dist > dist[current_cidade]:
            continue

        for vizinho, custo in adjacencias.get(current_cidade, []):  # Usando .get para evitar KeyError
            dist_vizinho = current_dist + custo
            if dist_vizinho < dist[vizinho]:
                dist[vizinho] = dist_vizinho
                heapq.heappush(pq, (dist_vizinho, vizinho))

    return dist.get(destino, None)  # Retorna None se o destino não for encontrado

if __name__ == "__main__":
    cidade_origem, cidade_destino, adjacencias = ler_entrada2()
    
    if cidade_origem and cidade_destino and adjacencias:
        print(f"Cidade origem: {cidade_origem}")
        print(f"Cidade destino: {cidade_destino}")
        custo_minimo = dijkstra(adjacencias, cidade_origem, cidade_destino)
        if custo_minimo is not None:
            print(f"O custo mínimo para transportar a mercadoria entre {cidade_origem} e {cidade_destino} é: {custo_minimo}")
        else:
            print("Não é possível calcular o custo mínimo.")
    else:
        print("Erro de leitura dos dados.")
