from collections import deque
class Solution(object):
    def shortestPathLength(self, graph):
        # Essa solução utiliza uma Busca em Largura (BFS) com máscara de bits para rastrear quais nós foram visitados
        # Por exemplo, em um grafo com 4 nós, a máscara de bits é composta por 4 bits, onde 0 significa não visitado e 1 significa visitado
        # O algorítmo utiliza uma técnica de programação dinâmica para armazenar os estados já visitados e não processá-los mais de uma vez, armazenando essa informação numa matriz 2^n x n
        # O objetivo do algoritmo é encontrar o caminho mais curto que visita todos os nós, ou seja, alcançar a máscara onde todos os bits estão definidos como 1
        # No caso de 4 nós, a máscara objetivo é '1111'

        n = len(graph)
        fila = deque()
        # Cria uma matriz 2^n x n, representando todas os estados possíveis em todos os nós (utilizando máscara de bits)
        visitados = [[False] * (1 << n) for i in range(n)]
        
        # Enfileira todos os nós com distância 0
        for i in range(n):
            fila.append((i, 1 << i, 0))  # (nó_atual, máscara_de_bits, distância)
            visitados[i][1 << i] = True
        
        mascara_fim = (1 << n) - 1  # Máscara onde todos os nós foram visitados
        
        while fila:
            # Desenfilera o primeiro da fila
            no_atual, mascara, dist = fila.popleft()
            if mascara == mascara_fim:
                return dist
            
            # Explora os vizinhos do nó atual
            for vizinho in graph[no_atual]:
                # Operação bit a bit para calcular a próxima máscara
                mascara_vizinho = mascara | (1 << vizinho)
                if not visitados[vizinho][mascara_vizinho]:
                    visitados[vizinho][mascara_vizinho] = True
                    fila.append((vizinho, mascara_vizinho, dist + 1))

solucao = Solution()
grafo = [[1,2,3],[0],[0],[0]]
print(solucao.shortestPathLength(grafo))