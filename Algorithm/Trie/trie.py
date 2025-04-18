# Trie example only populate lowercase letter
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        prev = self.root

        for char in word:
            pos = self.word_to_int(char)

            if not prev.children[pos]:
                prev.children[pos] = TrieNode()
            prev = prev.children[pos]
        
        prev.is_end_of_word = True
                
    def word_to_int(self, char):
        return ord(char) - ord("a")

    def search(self, word):
        prev = self.root

        for char in word:
            pos = self.word_to_int(char)
            prev = prev.children[pos]

            if not prev:
                return False
            
        return prev.is_end_of_word
    
    def start_with(self, prefix):
        prev = self.root

        for char in prefix:
            pos = self.word_to_int(char)
            prev = prev.children[pos]

            if not prev:
                return False
        
        return True
