class Node:
    def __init__(self, center):
        self.center = center
        self.left = None
        self.right = None

# Create the tree with string values
# Root
g = Node("a")
g.left = Node("b")
g.right = Node("c")

# Left subtree
g.left.left = Node("d")
g.left.right = Node("e")
g.left.right.right = Node("h")     # h is right child of e

# Right subtree
g.right.left = Node("f")           # f is left child of c
g.right.left.left = Node("i")      # i is left child of f
g.right.right = Node("g")          # g is right child of c
g.right.right.left = Node("j")

# Inorder: Left → Root → Right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.center, end=" ")
        inorder(node.right)

# Preorder: Root → Left → Right
def preorder(node):
    if node:
        print(node.center, end=" ")
        preorder(node.left)
        preorder(node.right)

# Postorder: Left → Right → Root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.center, end=" ")

# Run all
print("Inorder:")
inorder(g)

print("\nPreorder:")
preorder(g)

print("\nPostorder:")
postorder(g)
