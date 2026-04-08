class WordDictionary:

    def __init__(self):
        self.word = False
        self.children = dict()

    def addWord(self, word: str) -> None:
        trie = self

        for char in word:
            if char not in trie.children:
                trie.children[char] = WordDictionary()
            trie = trie.children[char]

        trie.word = True

    def search(self, word: str) -> bool:
        trie = self

        def search_util(j, trie):
            for i in range(j, len(word)):
                char = word[i]
                if char != '.':
                    if char not in trie.children:
                        return False
                    trie = trie.children[char]
                else:
                    for child in trie.children.values():
                        if search_util(i + 1, child):
                            return True
                    return False
            
            return trie.word

        return search_util(0, trie)
