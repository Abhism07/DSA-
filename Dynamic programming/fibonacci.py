'''
Dynamic Programming is mainly an optimization over plain recursion.
Wherever we see a recursive solution that has repeated calls for same inputs, 
we can optimize it using Dynamic Programming. The idea is to simply store the
results of subproblems, so that we do not have to re-compute them when needed later.
'''
def fibonnaci(n):
    #recursion approach
    if n<=1:
        return n
    return fibonnaci(n-1)+fibonnaci(n-2)  
  
    #by Dynamic programming approach
    fib=[0,1]
    
    for i in range (2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]
    
print(fibonnaci(9))    
