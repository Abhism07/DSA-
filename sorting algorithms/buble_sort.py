'''
Run a nested for loop to traverse the input array using two variables i and j,
 such that 0 ≤ i < n-1 and 0 ≤ j < n-1
If arr[j] is greater than arr[j+1] then swap these adjacent elements, else move on
Print the sorted arr
This algorithm is not suitable for large data sets as its average and worst-case
 time complexity is quite high.
 Time Complexity: O(N^2)
 space complexity:O(1)
'''
Arr=[]
n = int(input("Enter the number of elements:"))
for i in range (n):
    ele = int(input("enter elements:"))
    Arr.append(ele)
    
for i in range (n):
    
    for j in range(0,n-1):
        if (Arr[j] > Arr[j+1]): 
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
print("sorted Array:")
for i in range(len(Arr)):
    print(Arr[i],end=" ")
    
'''The above function always runs O(N2) time even if the array is sorted.
 It can be optimized by stopping the algorithm if the inner loop didn’t cause any swap.
  
  n = len(Arr)
    # Traverse through all array elements
    for i in range(n):
        swap = False
        for j in range(0, n-1):
            # traverse the array from 0 to n-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if (swap == False):
            break
 
 '''    