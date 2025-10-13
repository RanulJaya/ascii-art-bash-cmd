import os
import time

def mergeSort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    leftSort = arr[:mid]
    rightSort = arr[mid:]

    unmergeSortLeft = mergeSort(leftSort)
    unmergeSortRight = mergeSort(rightSort)

    return merge(unmergeSortLeft, unmergeSortRight)

def merge(left, right):

    result = []
    i = j = 0

    print("left: ")
    while i < len(left):
        result.append(left[i])
        print(result)
        i+=1

    print("right: ")
    while j < len(right):
        result.append(right[j])
        print(result)
        j+=1

    i = j = 0

    while i < len(result):
        j=0
        while j < i:
            if result[i] < result[j]:
                    placeholderVal = result[j]
                    result[j] = result[i]
                    result[i] = placeholderVal
            j+=1
        i+=1

    print(f"sorted: {result}")
    return result


unsortedArr = [12, 8, 9, 3, 11, 5, 4]
sortedArr = mergeSort(unsortedArr)
print(f"Final Sorted: {sortedArr}" )