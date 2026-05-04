class TrieNode:
    def __init__(self,val, is_end):
        self.val = val
        self.children = {}
        self.is_end = is_end

def find_user(node, target):
    for c in target:
        if c not in node.children:
            return False
        node = node.children[c]
    return node.is_end