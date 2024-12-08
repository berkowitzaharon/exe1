def parent(i):
    return (i - 1) // 2

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2

def heapify_down(heap, i, len_heap):
    comparisons_count = 0
    initializations_count = 0

    largest = i
    while True:
        left = left_child(i)
        right = right_child(i)

        comparisons_count +=1
        if left < len_heap and heap[left] > heap[largest]:
            largest = left

        comparisons_count +=1
        if right < len_heap and heap[right] > heap[largest]:
            largest = right
        
        if largest == i:
            break

        heap[i], heap[largest] = heap[largest], heap[i]
        initializations_count +=1
        i = largest
    return comparisons_count, initializations_count


def build_max_heap(arr):
    comparisons_count = 0
    initializations_count = 0

    last_parent = len(arr)//2 -1
    for i in range(last_parent, -1, -1):
        compar_count, init_count = heapify_down(arr, i, len(arr))
        comparisons_count += compar_count
        initializations_count += init_count
    
    return comparisons_count, initializations_count
    


def heap_sort(arr):
    comparisons_count, initializations_count = build_max_heap(arr)
    for heap_border in range(len(arr)-1, 0, -1):
        arr[0], arr[heap_border] = arr[heap_border], arr[0]
        initializations_count += 1
        compar_count, init_count = heapify_down(arr, 0, heap_border)
        comparisons_count += compar_count
        initializations_count += init_count
    
    return comparisons_count, initializations_count


