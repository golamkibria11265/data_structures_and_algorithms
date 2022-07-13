def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers_of_list = [11,10,12,45,30,25,90,67]
print(bubbleSort(numbers_of_list))
