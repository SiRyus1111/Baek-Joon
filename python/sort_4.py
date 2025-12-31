def selection_sort(arr):
    for i in range(len(arr)):
        min =  i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[j], arr[min] = arr[min], arr[j]
def insertion_sort_1(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
def insertion_sort_2(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
def quick_sort(arr,start,end):
    if start>=end:
        return
    l = start + 1
    r = end
    pivot = start
    while l <= end and arr[l] <= arr[pivot]:
        l+1
    while r > start and arr[r] >= arr[pivot]:
        r-1
    if r < l:
        arr[r], arr[pivot] = arr[pivot], arr[r]
    else:
        arr[r], arr[l] = arr[l], arr[r]
    quick_sort(arr, start, r - 1)
    quick_sort(arr, r + 1, end)