class Node:
    def __init__(self, data):
        self.data = data
        self.adress = None  # Corrected reference

class Singly:
    def __init__(self):
        self.head = None

    def tre(self, data):
        new_node = Node(data)
        new_node.adress = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.adress
        print("None")

# Example usage
li = Singly()
li.tre(76)
li.tre(50)
li.tre(30)
li.display()
