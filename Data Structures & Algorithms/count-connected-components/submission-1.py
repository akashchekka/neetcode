class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        count = 0
        visited = set()

        def build_adj_graph():
            for edge in edges:
                u = edge[0]
                v = edge[1]

                if not u in graph : graph[u] = []
                if not v in graph : graph[v] = []
                
                graph[u].append(v)
                graph[v].append(u)
        
        def dfs(node):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        build_adj_graph()
        for node in graph:
            if node not in visited:
                dfs(node)
                count += 1

        return count

        
