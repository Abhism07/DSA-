class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
def is_empty(head):
    return head is None

def insert(self,data):
    new_node=Node(data)
    new_node.next=head
    return new_node
    
def tail(self,data):
    new_node=Node(data)
    if is_empty(head):
        return new_node
    current =head
    while current.next is not None:
       current=current.next
    current.next=new_node
    return head

def pop(head):
    if is_empty(head):
        return head is None
    current=head
    while current is not None:
        if current.next.next==None:
            current.next=None
        current=current.next
    return head
            
          
def display(head):
    ele=[]
    current=head
    while current is not None:
        ele.append(current.data)
        current=current.next
    for i in range (len(ele)-1,-1,-1): 
        print(ele[i],end='\n')    
    
head=None
head=insert(head,1)
head=insert(head,2)   
head=insert(head,5)   
head=insert(head,9)  
head=tail(head,55)
display(head)
