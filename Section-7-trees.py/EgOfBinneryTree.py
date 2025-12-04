class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(6)
a = Node(5)
b = Node(2)
root.left=a
root.right=a
print(root.data)
print(root.right.data)
# print(root.right.data)