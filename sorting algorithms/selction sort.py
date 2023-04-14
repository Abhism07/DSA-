'''
 best-case and average-case time complexity of O(n^2),
 making it efficient for small data sets.
 It has a time complexity of O(n^2) in the worst and average case
 which makes it less efficient for large data sets.
'''
Arr=[]
n = int(input("Enter the number of elements:"))
for i in range (n):
    ele = int(input("enter elements:"))
    Arr.append(ele)
    
for i in range (len(Arr)):
	ind=i
	for j in range (i+1,len(Arr)):
		if (Arr[ind]>Arr[j]):
			ind=j
	Arr[i],Arr[ind] = Arr[ind],Arr[i]
print("Sorted Array:")
for i in range (len(Arr)):
	print("%d" %Arr[i],end=" ")
	
