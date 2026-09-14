from collections import deque
from heapq import heappush, heappop, heapify

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-count for count in counter.values()]
        heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1
            if max_heap:
                freq = heappop(max_heap)
                freq += 1 # processing 1 task

                if freq != 0:
                    q.append((freq, time + n))

            while q and q[0][1] == time:
                element, _ = q.popleft()
                heappush(max_heap, element)

        return time