class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert(head,data):
    new_node=Node(data)
    if not head:
        head=new_node
        new_node.next=head
    else:
        current =head
        while current.next!=head:
            current=current.next
        current.next=new_node
        new_node.next=head
    return head
    
def traverse(head):
    current=head
    while True:
        print(current.data)
        current=current.next
        if current.next==head:
            break

head=None
head=insert(head,1)            
head=insert(head,5)
head=insert(head,6) 
head=insert(head,3)
traverse(head)          
