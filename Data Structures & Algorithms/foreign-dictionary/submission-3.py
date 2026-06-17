class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegree = {c: 0 for w in words for c in w}
        nodes = set()

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    indegree[w2[j]] += 1
                    nodes.add(w1[j])
                    nodes.add(w2[j])
                    break
                j += 1

        q = deque([node for node in indegree if indegree[node] == 0])
        res = []
        while q:
            current = q.popleft()
            res.append(current)

            for nei in graph[current]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return ''.join(res) if len(res) == len(indegree) else ""