class Solution(object):
    def findRedundantConnection(self, edges):
        # Inicializa o array de pais onde cada nó é seu próprio pai
        n = len(edges)
        pai = [i for i in range(n + 1)]  # Índices de 0 a n

        # Função recursiva para encontrar o representante do conjunto que contém o nó 'u'
        def encontrar(u):
            if pai[u] != u:
                pai[u] = encontrar(pai[u]) 
            return pai[u]

        # Função para unir os conjuntos que contêm os nós 'u' e 'v'
        def unir(u, v):
            raiz_u = encontrar(u)
            raiz_v = encontrar(v)
            if raiz_u == raiz_v:  # Se pertencerem ao mesmo conjunto, um ciclo é detectado
                return False
            pai[raiz_u] = raiz_v  # Une os conjuntos
            return True

        # Percorre cada aresta e tenta unir os conjuntos
        for u, v in edges:
            if not unir(u, v):
                # Aresta redundante encontrada
                return [u, v]

grafo = [[1,2],[2,3],[3,4],[1,4],[1,5]]
solucao = Solution()
print(solucao.findRedundantConnection(grafo))