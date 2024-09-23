class Trie:

    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        node = self.children
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        
        node["end"] = True
        
    def search(self, word: str) -> bool:
        node = self.children
        for c in word:
            if c not in node:
                return False
            node = node[c]
        
        return "end" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.children
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        
        return True
