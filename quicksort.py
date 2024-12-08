from random import randint
def randomise_parttittion (arr,start,end):
    counter_comprarisons = 0
    counter_initializations = 0

    pivot = randint (start,end)
    # pivot = 0
    if pivot!= len(arr)-1:
        arr[pivot],arr[end]=arr[end],arr[pivot]#רק אם הוא לא אחרון
        counter_initializations += 2
    i,j = start,start
    k = end-1

    while j<=k:
        # print (1,arr,pivot,k)
        counter_comprarisons+=1
        if arr [j]<arr[end]:
            arr[i],arr[j]=arr[j],arr[i]
            counter_initializations += 2
            i+=1
            j+=1
        elif arr[j]> arr[end]:
            arr[j],arr[k] = arr[k],arr[j]
            counter_initializations += 2
            k-=1
        else:
            j+=1
    arr[end],arr[j]=arr[j],arr[end]
    counter_initializations += 2

    return i,j,counter_comprarisons,counter_initializations

def quick_sort (arr,start,end):
    if end<=start:
        return 0,0
    i,j,counter_comprarisons,counter_initializations = randomise_parttittion(arr,start,end)
    l_counter_p ,l_counter_i = quick_sort(arr,start,i-1)
    r_counter_p ,r_counter_i = quick_sort(arr,j+1,end)
    
    return l_counter_p+r_counter_p+counter_comprarisons,l_counter_i+r_counter_i+counter_initializations


a= [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-7,7]
comprarisons , initializations = (quick_sort(a,0,len(a)-1))
# (quicksort(a,0,len(a)-1))
print(a)
print(comprarisons,initializations)
