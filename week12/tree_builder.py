class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left  = left
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
            # if equal, do nothing (no duplicates)
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
                # found the node
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # two children: replace with inorder successor
                succ = self.findMin(node.right)
                node.value = succ.value
                node.right = delete_helper(node.right, succ.value)
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
        print()

    def printLevels(self):
        from collections import deque
        if self.root is None:
            print("The tree is empty")
            return

        queue = deque([self.root])
        level = 0
        while queue:
            size = len(queue)
            print(f"Level {level}:", end=" ")
            for _ in range(size):
                n = queue.popleft()
                print(n.value, end=" ")
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            print()
            level += 1

    def to_string(self):
        """Return the (left,value,right) representation, with '-' for empty."""
        def recurse(node):
            if node is None:
                return "-"
            left  = recurse(node.left)
            right = recurse(node.right)
            return f"({left},{node.value},{right})"
        return recurse(self.root)


if __name__ == "__main__":
    # --- Test case ---
    test_data = [3, 5, 4, 2, 8]
    bst_test = BinarySearchTree()
    for v in test_data:
        bst_test.insert(v)

    print("Test case input: ", test_data)
    print("Test case output:", bst_test.to_string())
    print()

    # --- Actual input data ---
    actual_data = [26, 7, 19, 23, 24, 20, 14, 25, 10, 11, 17, 28, 16, 31,
                   1, 22, 12, 8, 5, 4, 18, 13, 9, 15, 30, 27, 2, 3, 6, 21, 29]
    bst_actual = BinarySearchTree()
    for v in actual_data:
        bst_actual.insert(v)

    print("Actual input: ", actual_data)
    print("Actual output:", bst_actual.to_string())
