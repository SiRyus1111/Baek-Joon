def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(min_index + 1,len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
def insertion_sort_1(array):
    for i in range(1, len(array)):
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
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
def quick_sort(arr,start,end):
    if start>=end:
        return
    pivot = start
    left = start+1
    right = end
    while left<=right:
        while left <= end and arr[pivot] >= arr[left]:
            left += 1
        while right > start and arr[pivot] <= arr[right]:
            right -= 1
        if right < left:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)