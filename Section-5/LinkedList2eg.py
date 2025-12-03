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

# insert at start
newNode = Node(4)
newNode.next = head
head = newNode

# insert at end
newNode = Node(11)
curr = head
while curr.next!=None:
    curr = curr.next
curr.next = newNode

# insert at kth index
newNode = Node(7)
k = 4
curr = head
for i in range(k-2):
    curr = curr.next
newNode.next = curr.next
curr.next = newNode

printLL(head)