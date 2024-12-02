#include <vector>
#include <queue>
#include <climits> // Para usar INT_MAX
using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // 1. Construção do grafo como lista de adjacências
        vector<vector<pair<int, int>>> graph(n + 1); // Usamos 1-indexed para os nós (1 até n)
        
        for (const auto& time : times) {
            int u = time[0], v = time[1], w = time[2];
            graph[u].push_back({v, w});
        }
        
        // 2. Inicializa a fila de prioridade e o vetor de distâncias
        vector<int> distances(n + 1, INT_MAX);  // Inicializa as distâncias como infinito
        distances[k] = 0;  // O tempo para o nó de origem é 0
        
        // heap para Dijkstra
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, k}); // A partir do nó k, com distância 0
        
        // 3. Algoritmo de Dijkstra
        while (!pq.empty()) {
            auto [curr_dist, node] = pq.top();
            pq.pop();
            
            // Se a distância atual já for maior que a melhor encontrada, ignorar
            if (curr_dist > distances[node]) {
                continue;
            }
            
            // Atualizar os vizinhos
            for (const auto& [neighbor, weight] : graph[node]) {
                int new_dist = curr_dist + weight;
                if (new_dist < distances[neighbor]) {
                    distances[neighbor] = new_dist;
                    pq.push({new_dist, neighbor});
                }
            }
        }
        
        // 4. Verificar a resposta
        int max_dist = 0;
        for (int i = 1; i <= n; ++i) {
            if (distances[i] == INT_MAX) {
                return -1; // Se algum nó não foi alcançado, retorna -1
            }
            max_dist = max(max_dist, distances[i]);
        }
        
        return max_dist;
    }
};
