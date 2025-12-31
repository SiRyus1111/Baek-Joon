def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(min_index + 1,len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
def insertion_sort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j]<array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break