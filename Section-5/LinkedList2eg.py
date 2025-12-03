class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    curr = head
    while curr!=None:
        print(curr.data, end=" -> ")
        curr = curr.next
    print()

a = Node(5)
b = Node(6)
c = Node(8)


a.next = b
b.next = c
head = a

printLL(head)