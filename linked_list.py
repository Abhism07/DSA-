class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_empty(head):
    return head is None

def insert_at_head(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_at_tail(head, data):
    new_node = Node(data)

    if is_empty(head):
        return new_node

    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node

    return head

def delete(head, data):
    if is_empty(head):
        return None

    if head.data == data:
        return head.next

    current = head
    while current.next is not None:
        if current.next.data == data:
            current.next = current.next.next
            return head
        current = current.next

    return head

def search(head, data):
    current = head
    while current is not None:
        if current.data == data:
            return True
        current = current.next
    return False

def display(head):
    elements = []
    current = head
    while current is not None:
        elements.append(current.data)
        current = current.next
    print(elements)
head = None

head = insert_at_head(head, 3)
head = insert_at_head(head, 2)
head = insert_at_head(head, 1)

head = insert_at_tail(head, 4)
head = insert_at_tail(head, 5)

head = delete(head, 3)

print(search(head, 2)) 
print(search(head, 6))  

display(head)  
