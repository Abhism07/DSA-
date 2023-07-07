size=5
def create_stack():
	return []*size

def is_empty(stack):
	return len(stack)==0
	
def push(stack,item):
	stack.append(item)
    
def pop(stack):
	if is_empty(stack):
	 return "stack is empty" 
	return stack.pop()
def peek(stack):
    if is_empty(stack):
        return "Stack is empty"
    if (len(stack)>size):
        print("stack overflow.") 
 
    return stack[::-1]

mystack=create_stack()

print(is_empty(mystack))
push(mystack,10)
push(mystack,1)
push(mystack,18)
push(mystack,15)
push(mystack,17)
push(mystack,19)

print(peek(mystack))	
	
