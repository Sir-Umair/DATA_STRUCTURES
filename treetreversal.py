class Node:
    def __init__(self, center):
        self.center = center
        self.left = None
        self.right = None

# Create the tree with string values
g = Node("a")
g.left = Node("b")
g.right = Node("c")
g.left.left = Node("d")
g.left.right = Node("e")
g.left.left.left = Node("h")
g.right.left = Node("f")
g.right.right = Node("g")
g.right.left.right = Node("i")
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
