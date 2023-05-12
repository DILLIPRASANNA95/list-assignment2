list1=[(1,5),(2,1),(3,4),(4,3),(5,2)]
print(list1)
res=[lis[1]for lis in list1]

for i in range(len(list1)):

    for j in range (i,len(list1)):

     if(res[i]>res[j]):
        temp=list1[i]
        list1[i]=list1[j]
        list1[j]=temp

        temp=res[i]
        res[i]=res[j]
        res[j]=temp
        
        print(list1)