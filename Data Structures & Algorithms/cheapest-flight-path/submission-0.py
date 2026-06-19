class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [set() for _ in range(n)]
        for frm, to, price in flights:
            graph[frm].add((to, price))

        dist = [float('inf')] * n
        print(len(dist))

        q = deque()
        # (stops, node, dst)
        q.append((0, src, 0))

        while q:
            stop, curr_node, curr_dist = q.popleft()

            for nei_node, nei_dst in graph[curr_node]:
                if curr_dist + nei_dst < dist[nei_node] and stop <= k:
                    dist[nei_node] = curr_dist + nei_dst
                    q.append((stop + 1, nei_node, dist[nei_node]))

        return -1 if dist[dst] == float('inf') else dist[dst]