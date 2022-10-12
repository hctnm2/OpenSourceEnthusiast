# Python insertion sorting algorithm
def insertion_sort(arr):
    # Step through the array starting at the second element
    for i in range(1, len(arr)):
        # Element to be inserted
        elem = arr[i]

        # iterator for sorted portion of array
        j = i - 1

        # Insert elem into the correct position within
        # the sorted half of the array
        while j >= 0 and arr[j] > elem:
            # Shift elem down an index
            arr[j + 1] = arr[j]
            j -= 1

        # insert elem in correct index
        arr[j + 1] = elem

    return arr

# test insertion sorting algorithm
arr = [12, 23, 40, 25, 27, 15, 4, 26, 43, 36]
print("Sorting: ", arr)
print("result: ", insertion_sort(arr))
