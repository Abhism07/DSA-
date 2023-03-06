''' Linked List '''
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_beg( self,data):
        node = Node(data,self.head)
        self.head=node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data,None)
        
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
            
    def get_len(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
            
        return count    
        
    def remove_at(self,index):
        if (index<0 or index>self.get_len()):
            raise Exception('Invalid index')
        if index==0:
            self.head=self.head.next
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.next = itr.next.next
                break
            itr=itr.next
            count+=1
                
    def insert_at (self,index,data):
        if (index<0 or index>self.get_len()):
            raise Exception('Invalid index')
        if index==0:
            self.insert_at_beg(data)
            return
        itr=self.head
        count=0
        while itr:
            if count == index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr = itr.next 
            count+=1
      
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
            
        itr = self.head
        llstr=''
        
        while itr:
            llstr+=str(itr.data)+"-->"
            itr=itr.next
        print(llstr)

if __name__=='__main__':
            ll = linkedlist()
            ll.insert_at_beg(55)
            ll.insert_at_beg(99)
            ll.insert_at_end(78)
            ll.insert_values(['Mango','Apple','Banana','Cherry'])
            ll.remove_at(2)
            ll.insert_at(0,'Abhishek')
            ll.insert_at(6,77)
            ll.print()
            print(ll.get_len())