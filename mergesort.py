def merge (arr1,arr2):
    i = 0
    j = 0
    counter_comprarisons = 0
    counter_initializations = 0
    arr_res = []
    while i <len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr_res.append(arr1[i])
            i+=1
        else:
            arr_res.append(arr2[j])
            j+=1
        counter_comprarisons +=1
        counter_initializations +=1
    if i < len(arr1):
        counter_initializations += len(arr1)-i
    elif j < len(arr2):
        counter_initializations += len(arr2)-j

    return arr_res + arr1[i:]+arr2[j:],counter_comprarisons,counter_initializations

def mergesort (arr):

    if len(arr)<=1:
        return arr,0,0
    mid = len(arr)//2
    arrLeft,l_counter_comprarisons,l_counter_initializations = mergesort(arr[:mid])
    arrRight,r_counter_comprarisons,r_counter_initializations = mergesort(arr[mid:])
    arrnew, counter_comprarisons,counter_initializations = merge (arrLeft,arrRight)
    new_counter_compra = l_counter_comprarisons+r_counter_comprarisons+counter_comprarisons
    new_counter_initi = l_counter_initializations+r_counter_initializations+counter_initializations
    return arrnew,new_counter_compra,new_counter_initi

def merge_sort (arr):
    newArr,counter_comprarisons,counter_initializations  = mergesort(arr)
    arr[:] =newArr
    return counter_comprarisons,counter_initializations
    
a=[9,8,7,6,5,4]
print (merge_sort(a))
print (a)