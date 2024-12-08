def insertion_sort(arr):
    counter_comprarisons = 0
    counter_initializations = 0
    for i in range(1,len(arr)):
        k = arr[i]
        for j in range(i-1,-1,-1):
            counter_comprarisons +=1    
            if arr[j] > k:
                counter_initializations+=1
                arr[j+1] = arr[j]
            else:
                arr[j+1] = k
                break
        else:
            arr[0]=k 
    return counter_comprarisons,counter_initializations

a= [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-7,7]
counter1 , counter2 = insertsort(a)
print (a)
print(counter1," ",counter2 )
