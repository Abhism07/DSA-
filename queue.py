def cre_qu():
	return []

def is_empty(qu):
	return len(qu)==0
def push(qu,item):
	qu.append(item)
def pop(qu):
	return qu.pop(0)
def peek(qu):
    return qu[::-1]

my_qu=cre_qu()
push(my_qu,1)
push(my_qu,2)
push(my_qu,6)
push(my_qu,5)
pop(my_qu)
pop(my_qu)
print(peek(my_qu))
