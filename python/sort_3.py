def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
def insertion_sort_1(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break
def insertion_sort_2(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j>=0 and array[j]>key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key