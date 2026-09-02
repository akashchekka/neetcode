class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        def children(lock: str):
            res = []
            for i in range(len(lock)):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        visited = set(['0000'])
        exclude = set(deadends)
        q = deque()
        q.append(('0000', 0))
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visited and child not in exclude:
                    visited.add(child)
                    q.append((child, turns + 1))

        return -1