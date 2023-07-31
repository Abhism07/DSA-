'''Binary search:Time complexity O(log n),
 Binary Search is a searching algorithm used in a sorted array 
by repeatedly dividing the search interval in half.
 sort the array and set low index to first element and 
high index to last element.Set the middle index to the average of the low and high 
indices.If the element at the middle index is the target element, return the middle 
index.If the target element is less than the element at the middle index, set the high
index to the middle index – 1.If the target element is greater than the element at
 the middle index, set the low index to the middle index + 1.'''
 
def binary_search():
    n = int(input("Enter the number of elements to insert in the list: "))
    lst = []
    for i in range(n):
        e = int(input("Enter key element: "))
        lst.append(e)
    print("List:", lst)

    key = int(input("Enter the number you want to search: "))
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == key:
            print("Element found at index", mid)
            return  # Return immediately after finding the element
        elif lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print("Element not found")

binary_search()

       
