class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0

        stop_to_bus = defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_bus[stop].add(bus)
        
        visited_bus = set()
        visited_stop = set()
        q = deque()

        visited_stop.add(source)
        q.append(source)
        res = 0

        while q:
            res += 1

            for _ in range(len(q)):
                curr_stop = q.popleft()
                for bus in stop_to_bus[curr_stop]:
                    if bus in visited_bus: continue
                    visited_bus.add(bus)

                    for next_stop in routes[bus]:
                        if next_stop == target: return res
                        visited_stop.add(next_stop)
                        q.append(next_stop)
        
        return -1
        