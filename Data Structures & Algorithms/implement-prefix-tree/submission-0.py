class PrefixTree:

    def __init__(self):
        self.isEnd = False
        self.children = dict()

    def insert(self, word: str) -> None:
        trie = self

        for char in word:
            if char not in trie.children:
                trie.children[char] = PrefixTree()
            trie = trie.children[char]

        trie.isEnd = True

    def search(self, word: str) -> bool:
        trie = self

        for char in word:
            if char not in trie.children:
                return False
            trie = trie.children[char]

        return trie.isEnd

    def startsWith(self, prefix: str) -> bool:
        trie = self

        for char in prefix:
            if char not in trie.children:
                return False
            trie = trie.children[char]

        return True
        