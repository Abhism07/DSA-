'''Binary search:Time complexity O(log n),
 Binary Search is a searching algorithm used in a sorted array 
by repeatedly dividing the search interval in half.
 sort the array and set low index to first element and 
high index to last element.Set the middle index to the average of the low and high 
indices.If the element at the middle index is the target element, return the middle 
index.If the target element is less than the element at the middle index, set the high
index to the middle index – 1.If the target element is greater than the element at
 the middle index, set the low index to the middle index + 1.'''
 
def binsearch():    
    list=[]
    n=int(input("Enter the number of elements to insert list:"))
    for i in range (n):
        e = int(input("enter key element:"))
        list.append(e)
    print(list)
    key=int(input("Enter the number you want to search:"))
    low=0
    high=len(list)-1
    mid=(high+low)//2
    while (high-low >1):
        if list[mid] < key:
            low=mid+1
        else:
            high=mid
    if(list[low]==key):
        print("Element found at index",low)
    elif(list[high]==key):
        print("Element found at index",high)
    else:
        print("Element not found")
            
binsearch()     
       