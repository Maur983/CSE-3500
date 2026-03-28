from collections import deque
import itertools
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def preorder(self,node):
        if not node:
            return
        print(node.value)
        self.preorder(node.left)
        self.preorder(node.right) 
    
    def inorder(self,node):
        if not node:
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)
    
    def postorder(self,node):
        if not node:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value)

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
def get(node, key):
    if node is None:
        return
    
    elif key == node.key:
        return node
    
    elif key < node.key:
        return get(node.left, key)
    
    else: #Or elif key> node.key
        return get(node.right, key)

def insert(node, key):
    if node is None:
        return BSTNode(key)

    elif key < node.key:
        node.left = insert(node.left, key)
    
    elif key > node.key:
        node.right = insert(node.right, key)
    return node

def min_node(node):
    while node.left:
        node = node.left
    return node

def remove(node,key):
    if node is None:
        return
    
    elif key < node.key:
        node.left = remove(node.left, key)
    
    elif key > node.key:
        node.right = remove(node.right, key)
    
    else: # elif key == node.key:
        #case 1 leaf
        if node.left is None and node.right is None:
            return
        #case 2 one child
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        #case 3 two children
        else:
            successor = min_node(node.right)
            node.key = successor.key
            node.right = remove(node.right, successor.key)
    return node

def rotate_right(y): #y is root
    # Getting variables
    x = y.left
    T2 = x.right
    # Perform rotation
    x.right = y
    y.left = T2
    return x

def rotate_left(x): #x is root
    # Getting variables
    y = x.right
    T2 = y.left
    # Perform rotation
    y.left = x
    x.right = T2
    return y

class AVLNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
    
def height(node):
    if node is None:
        return 0
    return node.height

def get_balanced(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

def rotate_right_balanced(y): #y is root
    # Getting variables
    x = y.left
    T2 = x.right
    # Perform rotation
    x.right = y
    y.left = T2
    #Update heights
    y.height = 1 +max(height(y.left), height(y.right))
    x.height = 1 +max(height(x.left), height(x.right))
    return x

def rotate_left_balanced(x): #x is root
    # Getting variables
    y = x.right
    T2 = y.left
    # Perform rotation
    y.left = x
    x.right = T2
    #Update heights
    y.height = 1 +max(height(y.left), height(y.right))
    x.height = 1 +max(height(x.left), height(x.right))
    return y

def insert_balance(node,key):
    if node is None:
        return AVLNode(key)

    elif key < node.key:
        node.left = insert_balance(node.left, key)
    
    elif key > node.key:
        node.right = insert_balance(node.right, key)
    else:
        return node

    node.height = 1+max(height(node.left), height(node.right))
    balance = get_balanced(node)
    #Single rotations
    if balance >1 and key < node.left.key:
        return rotate_right_balanced(node)
    elif balance <-1 and key > node.right.key:
        return rotate_left_balanced(node)
    #Double Rotations
    elif balance >1 and key >node.left.key:
        node.left = rotate_left_balanced(node.left)
        return rotate_right_balanced(node)
    elif balance <-1 and key < node.right.key:
        node.right = rotate_right_balanced(node)
        return rotate_left_balanced(node)
    return node
def search(root,value): #Space O(h) not optimal
    if root is None:
        return False
    elif root.key == value:
        return True
    elif root.key>value:
        return search(root.left, value)
    else:
        return search(root.right, value)
def search_iter(root,value): #Time is O(h) and the Space is now O(1)
    current = root
    while current:
        if value == current.key:
            return True
        elif value < current.key:
            current = current.left
        else:
            current = current.right
    return False
def foo(root, depth=0): #Time O(h) Space O(h)
    if root is None:
        return 0
    return depth + foo(root.left, +1), foo(root.right, +1)
def foo_iter(root):
    if  root is None:
        return 0
    total = 0
