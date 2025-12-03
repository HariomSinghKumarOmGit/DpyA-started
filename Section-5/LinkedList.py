class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(5)
b = Node(6)
c = Node(8)


a.next = b
b.next = c
head = a

print(head.data)
print(head.next.data)
print(head.next.next.data)