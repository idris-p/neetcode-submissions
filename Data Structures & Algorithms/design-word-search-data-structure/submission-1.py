class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.isWord = False
        

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                pointer.children[letter] = TrieNode(letter)
            pointer = pointer.children[letter]
        pointer.isWord = True

    def search(self, word: str) -> bool:
        result = False
        pointer = self.root

        print("Word:", word)
        def explore(i, path):
            nonlocal pointer
            nonlocal result
            print("Exploring:", path)
            print("Pointer:", pointer.char)
            print("i:", i)

            if i == len(word):
                if pointer.isWord:
                    result = True
                    print("Word found")
                print("Backtracking")
                return
            if i != 0 and word[i - 1] != pointer.char and word[i - 1] != ".":
                print("Backtracking")
                return

            temp = pointer
            if word[i] in pointer.children:
                pointer = pointer.children[word[i]]
                print()
                explore(i + 1, path + word[i])
            elif word[i] == ".":
                print("Going to explore:", list(pointer.children.keys()))
                for child in pointer.children:
                    print("Children:", list(pointer.children.keys()))
                    pointer = pointer.children[child]
                    # pointer = temp
                    print()
                    explore(i + 1, path + word[i])
                    pointer = temp
                    if result:
                        break
            pointer = temp
            
            
        explore(0, "")
        print(result)
        return result