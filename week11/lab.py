from collections import defaultdict

class BinaryTree:
    
    def __init__(self, root_obj):
            self.key = root_obj
            self.left_child = None
            self.right_child = None
            
    def insert_left(self, new_node): #right is similar
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child

    def insert_right(self, new_node): #right is similar
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child

def preorder(tree):
    if tree:
        print(tree.key,end=' ')
        preorder(tree.left_child)
        preorder(tree.right_child)
        
def inorder(tree):
    if tree:
            inorder(tree.left_child)
            print(tree.key,end=' ')
            inorder(tree.right_child)
            
def postorder(tree):
    if tree:
            postorder(tree.left_child)
            postorder(tree.right_child)
            print(tree.key, end=' ')

def tree_depth(node):
    if node is None:
        return -1
    else:
        left_depth = tree_depth(node.left_child)
        right_depth = tree_depth(node.right_child)
        return 1 + max(left_depth, right_depth)
    