class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
    
    def search(self, word): #Time O(n) looping through the word length Space 
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
            return node.is_end
            #if node.is_end: this another way to it
                #return True
            #else:
                #return False