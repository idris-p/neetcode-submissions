class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                pointer.children[letter] = TrieNode(letter)
            pointer = pointer.children[letter]
        pointer.children["*"] = None

    def search(self, word: str) -> bool:
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return "*" in pointer.children

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for letter in prefix:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return True