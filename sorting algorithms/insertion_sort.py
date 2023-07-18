'''Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
The worst-case time complexity of the Insertion sort is O(N^2)
The average case time complexity of the Insertion sort is O(N^2)
The time complexity of the best case is O(N).'''

def insertion_sort(arr):
	for i in range(1,len(arr)):
		key=arr[i]
		j=i-1
		while j>=0 and key < arr[j]:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key

arr=[]
n=int(input("Enter no. of eements to add:"))
for _ in range (n):
    ele=int(input("Enter element:"))
    arr.append(ele)
print("sorted array:",end="\n")
insertion_sort(arr)
for i in range(len(arr)):
    print(arr[i],end=" ")
