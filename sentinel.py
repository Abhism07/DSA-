''' sentinel search:In this search, the last element of the array is replaced with the
 element to be searched and then the linear search is performed on the array without 
 checking whether the current index is inside the index range of the array or not 
 because the element to be searched will definitely be found inside the array even 
 if it was not present in the original array since the last element got replaced with it. 
 So, the index to be checked will never be out of the bounds of the array. 
 The number of comparisons in the worst case there will be (N + 2). '''
 
def sentinelsearch():
    list=[]
    n=int(input("Enter the number of elements to insert list:"))
    for i in range (n):
        e = int(input("enter key element:"))
        list.append(e)
    print(list)
    key=int(input("Enter the number you want to search:"))
    last = list[n-1]
    list[n-1]=key #assigning key value to the last position in list
    i=0
    while (list[i]!=key):
        i+=1
    list[n-1]=last #put last element back to position
    if((i<n-1) or (list[n-1]==key)):
        print(key,"found at index",i)
    else:
        print("Element not found")
            
sentinelsearch()    