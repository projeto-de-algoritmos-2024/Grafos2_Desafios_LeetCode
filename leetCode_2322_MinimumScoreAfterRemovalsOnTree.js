/**
 * @param {number[]} nums
 * @param {number[][]} edges
 * @return {number}
 */
const minimumScore = function (nums, edges) {
  const n = nums.length;
  let ans = Infinity;
  const visited = Array(n).fill(0);
  const pc = [];
  const adj = Array.from({ length: n }, () => []);
  const child_xor = Array(n).fill(0);
  const childs = Array.from({ length: n }, () => Array(n).fill(false));
  const { min, max } = Math;
  const par = Array(n).fill(0);

  // Construindo o grafo
  for (const edge of edges) {
    adj[edge[0]].push(edge[1]);
    adj[edge[1]].push(edge[0]);
  }

  // DFS para calcular os XORs das subárvores
  dfs(0);

  // Iterando sobre todas as combinações de pares de arestas para remover
  for (let i = 0; i < pc.length; i++) {
    for (let j = i + 1; j < pc.length; j++) {
      // Pegando os nós que são filhos após remover as arestas i e j
      const a = pc[i][1], b = pc[j][1]; 
      let xa = child_xor[a], xb = child_xor[b], xc = child_xor[0];

      // Se a aresta conecta as duas subárvores, atualiza os XORs
      if (childs[a][b]) {
        (xc ^= xa), (xa ^= xb);
      } else {
        (xc ^= xa), (xc ^= xb);
      }

      // Atualiza a resposta com o menor score possível
      ans = min(max(xa, max(xb, xc)) - min(xa, min(xb, xc)), ans);
    }
  }

  return ans;

  // Função DFS para calcular o XOR das subárvores
  function dfs(i) {
    let ans = nums[i];
    visited[i] = true;

    // Marca os pais das subárvores
    for (let p of par) {
      childs[p][i] = true;
    }

    par.push(i);

    // Recursivamente calcula os XORs dos filhos
    for (let child of adj[i] || []) {
      if (!visited[child]) {
        pc.push([i, child]);
        ans ^= dfs(child); // XOR do nó atual com a subárvore
      }
    }

    par.pop();
    return (child_xor[i] = ans);
  }
};
