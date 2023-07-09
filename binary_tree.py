class binary_tree:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None


root=binary_tree("A")
node_b=binary_tree("B")
node_c=binary_tree("C")
node_d=binary_tree("D")
node_e=binary_tree("E")
node_f=binary_tree("F")

root.left = node_b
root.right = node_c
node_b.left = node_d
node_b.right = node_e
print("inorder")
def inorder(node):
	if node is None:
		return 
	inorder(node.left)
	print(node.data)
	inorder(node.right)
inorder(root)
print("preorder_traversal")
def preorder_traversal(node):
    if node is None:
        return
    print(node.data)  # Process current node
    preorder_traversal(node.left)  # Traverse left subtree
    preorder_traversal(node.right)  # Traverse right subtree
preorder_traversal(root)
print("postorder traversal")	
def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)  # Traverse left subtree
    postorder_traversal(node.right)  # Traverse right subtree
    print(node.data)  # Process current node
postorder_traversal(root)