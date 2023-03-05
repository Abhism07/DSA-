def search():    
    list=[]
    n=int(input("Enter the number of elements to insert list:"))
    for i in range (n):
        e = int(input("enter key element:"))
        list.append(e)
    print(list)
    list2=[]
    flag=False
    key=int(input("Enter the number you want to search:"))
    for i in range (len(list)):
        if key==list[i]:
            flag=True
            list2.append(i)
            break   
    if flag==True:
        for i in list2:
            print(key,"found at index",i)
    else:
        print("key is not found")
search()