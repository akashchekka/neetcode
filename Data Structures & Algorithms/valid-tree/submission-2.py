class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        visit = set()
        graph = {i: [] for i in range(n)}
        for edge in edges:
            u = edge[0]
            v = edge[1]

            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)

            for nei in graph[node]:
                if nei == parent: continue
                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n