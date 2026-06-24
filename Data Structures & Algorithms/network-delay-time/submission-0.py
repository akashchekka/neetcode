class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from heapq import heappush, heappop
        res = [float('inf')] * (n+1)

        graph = {i+1: [] for i in range(n)}
        for n1, n2, time in times:
            graph[n1].append((n2, time))
        
        heap = []
        heappush(heap, (0, k))
        res[k] = 0
        while heap:
            time, curr_node = heappop(heap)

            if time > res[curr_node]: continue

            for nei_node, nei_time in graph[curr_node]:
                if time + nei_time < res[nei_node]:
                    res[nei_node] = time + nei_time
                    heappush(heap, (res[nei_node], nei_node))

        ans = max(res[1:])
        return ans if ans < float('inf') else -1