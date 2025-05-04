class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def insert_helper(node, value):
            if node is None:
                return TreeNode(value)
            if value < node.value:
                node.left = insert_helper(node.left, value)
            elif value > node.value:
                node.right = insert_helper(node.right, value)
            return node

        self.root = insert_helper(self.root, value)

    def deleteNode(self, value):
        def delete_helper(node, value):
            if node is None:
                return None
            if value < node.value:
                node.left = delete_helper(node.left, value)
            elif value > node.value:
                node.right = delete_helper(node.right, value)
            else:
                # node to delete found
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # two children: replace with inorder successor
                successor = self.findMin(node.right)
                node.value = successor.value
                node.right = delete_helper(node.right, successor.value)
            return node

        self.root = delete_helper(self.root, value)

    def findMin(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorderTraversal(self):
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            print(node.value, end=" ")
            inorder(node.right)

        inorder(self.root)
        print()  # newline after traversal

    def printLevels(self):
        if self.root is None:
            print("The tree is empty")
            return

        from collections import deque
        queue = deque([self.root])
        level = 0

        while queue:
            size = len(queue)
            print(f"Level {level}:", end=" ")
            level += 1

            for _ in range(size):
                node = queue.popleft()
                print(node.value, end=" ")
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            print()  # newline after each level

if __name__ == "__main__":
    bst = BinarySearchTree()
    # Inserting values
    for v in [2, 0, 5, 6, 1, 6, 2]:
        bst.insert(v)
        
    print("In-order:", end=" ")
    bst.inorderTraversal()

    # Level-order traversal
    bst.printLevels()
