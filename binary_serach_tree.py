class bst:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left=bst(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right=bst(data)
            else:
                self.right.insert(data)
root =bst(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(14)
root.insert(4)
root.insert(7)
root.insert(13) 

print("\ninorder traversal")
def inorder(node):
	if node is None:
		return 
	inorder(node.left)
	print(node.data,end=" ")
	inorder(node.right)
inorder(root)

print("\npreorder traversal")
def preorder_traversal(node):
    if node is None:
        return
    print(node.data,end=" ")  
    preorder_traversal(node.left)  
    preorder_traversal(node.right) 
preorder_traversal(root)

print("\npostorder traversal")	
def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)  
    postorder_traversal(node.right) 
    print(node.data,end=" ")  
postorder_traversal(root)