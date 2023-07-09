class Node:
	def __init__(self,data):
		self.data=data
		self.child=[]

	def insert(self,data):
		self.child.append(data)

root=Node("A")
node_b=Node("B")
node_c=Node("C")
node_d=Node("D")
node_e=Node("E")
node_f=Node("F")

root.insert(node_b)
root.insert(node_c)
node_b.insert(node_d)
node_c.insert(node_e)
node_c.insert(node_f)

def dfs(node):
    print(node.data)  
    for children in node.child:
        dfs(children)  
dfs(root)
