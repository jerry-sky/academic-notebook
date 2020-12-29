#!/usr/bin/env python3

from copy import deepcopy

is_count = 0

# Function to do insertion sort


def insertionSort(arr):
    global is_count
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            is_count += 1
        arr[j+1] = key


standard_count = 0


def standard(arr):
    global standard_count
    for i in range(0, len(arr)):
        a_i = arr[i]
        for j in range(i+1, len(arr)):
            a_j = arr[j]
            if a_i > a_j:
                standard_count += 1


merge_count = 0


def mergeSort(arr):
    global merge_count
    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            merge_count += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            merge_count += 1
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


counting_count = 0


def countSort(arr):
    global counting_count
    # The output character array that will have sorted arr
    output = [0 for i in range(256)]

    # Create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for i in range(256)]

    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[i] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]

    # Build the output character array
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        if ans[i] != output[i]:
            counting_count += 1
        ans[i] = output[i]
    return ans


arr = [5, 3, 5, 7, 1, 4, 8, 9, 12, 0, 4, 5, 2]
arr2 = deepcopy(arr)
arr3 = deepcopy(arr)

standard(arr)
insertionSort(arr2)
countSort(arr3)

print(is_count, standard_count, counting_count)
