'''
Merge sort is the sorting algorithm which uses divide and conquer method
using which it divides array int smaller sub partsand sorts them and then 
finally merge them at the end.
Merge sort is recursive algorithm.
The worst,average,best-case time complexity of merge sort is O(n*logn).
recurrence relation of merge sort is T(n)=2T(n/2)+θ(n).
'''
Arr=[]
n = int(input("Enter the number of elements:"))
for i in range (n):
    ele = int(input("enter elements:"))
    Arr.append(ele)
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
   
        mergesort(left)
        mergesort(right)
    
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1 
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
mergesort(Arr)
print("sorted array:")
for i in range (n):
    print(Arr[i],end=" ")        