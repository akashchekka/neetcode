class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        trie = self
        for char in word:
            if char not in trie.children:
                trie.children[char] = Trie()
            trie = trie.children[char]

        trie.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        res = set()
        visit = set()
        def explore(r, c, node, prefix):
            if (not (0 <= r < ROWS) or 
                not (0 <= c < COLS) or 
                board[r][c] not in node.children or 
                (r, c) in visit):
                return 

            visit.add((r, c))

            char = board[r][c]
            node = node.children[char]
            new_prefix = prefix + char
            if node.is_word:
                res.add(new_prefix)

            iters = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in iters:
                nr, nc = r + dr, c + dc
                explore(nr, nc, node, new_prefix)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                explore(r, c, trie, '')

        return list(res)
        