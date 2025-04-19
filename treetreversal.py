class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Create the tree with string values
g = Node("a")
g.left = Node("b")
g.right = Node("c")
g.left.left = Node("d")
g.left.right = Node("e")
g.right.left = Node("f")
g.right.right = Node("k")

# Inorder: Left → Root → Right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

# Preorder: Root → Left → Right
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

# Postorder: Left → Right → Root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

# Run all
print("Inorder:")
inorder(g)

print("\nPreorder:")
preorder(g)

print("\nPostorder:")
postorder(g)
