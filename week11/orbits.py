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
        
# Construct the binary tree
# I would need a relationship representation on a list to relate parent)child

def tree_map(data):
    """ From data, creates a map relating parent and child"""
    map = defaultdict(list)
    for relation in data:
        parent, child = relation.split(")")
        map[parent].append(child)
    
    return map

# After construction of adjancency list, need to construct the binary tree
# Need a node list to store unique nodes, I can use a wrapper so I can use more than 1 data file
# And create a local dict that can pass each recursion 

def construct_bt_wrapper(root_name, tree_map):
    """ 
        Wrapper for constructing a binary tree
        
        @params:
        root_name (str): Takes in the root name of the adjacency list
        tree_map (dict): parent)child representation to help construct the bt
        
        @returns: 
        root (BinaryTree node)
    """
    
    node_dict = {}
    
    def construct_bt(curr_node):
        if curr_node not in node_dict:
            node_dict[curr_node] = BinaryTree(curr_node)
        node = node_dict[curr_node]
        
        # Get its children and recursively insert as it childrens can act as subtrees
        children = tree_map.get(curr_node, []) # If no children, return empty list []
        # print(f"Children {children}")
        if len(children) > 0: # If atleast 1 children
            
            if children[0] not in node_dict:
                node.insert_left(children[0])
                node_dict[children[0]] = node.left_child
            construct_bt(children[0])
            
        if len(children) > 1: # If more than 1 children, we limit this to 2 children per node for our constraint, else it will not be binary tree
            if children[1] not in node_dict:
                node.insert_right(children[1])
                node_dict[children[1]] = node.right_child
            construct_bt(children[1])
            
        return node
    
    return construct_bt(root_name)

def tree_depth(node):
    if node is None:
        return -1
    else:
        left_depth = tree_depth(node.left_child)
        right_depth = tree_depth(node.right_child)
        return 1 + max(left_depth, right_depth)
    
def sum_depth(node, depth=0):
    if node is None:
        return 0
    
    return depth + sum_depth(node.left_child, depth + 1) + sum_depth(node.right_child, depth + 1)
    
        
# ========
# PART ONE
# ========
print("PART ONE") 
    
testData = open("11_test.txt", "r").read().strip().split('\n')
testMap = tree_map(testData)
testRoot = construct_bt_wrapper("COM", testMap)

data = open("11.txt", "r").read().strip().split('\n')
map = tree_map(data)
root = construct_bt_wrapper("COM", map)

# Questions asks for width of the planet, in this case its actually the depth of the binary tree
print(f"Tree depth for test case: {tree_depth(testRoot)}")
print(f"Tree depth for answer : {tree_depth(root)}")

# ========
# PART TWO
# ========
print("PART TWO")

# Question asks for number of orbits
# Basically what's the total number of preceding nodes to a current node, basically its parents/ancestors

# We can find the depth of each node and add them all up
print(f"Test case num of orbits: {sum_depth(testRoot)} ")
print(f"Num of orbits answer:  {sum_depth(root)}")