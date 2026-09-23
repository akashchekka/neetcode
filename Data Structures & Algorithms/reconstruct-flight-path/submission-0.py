class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict

        graph = defaultdict(list)
        for source, destination in sorted(tickets,reverse=True):
            graph[source].append(destination)

        itinerary = []
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            itinerary.append(airport)

        dfs('JFK')
        return itinerary[::-1]
