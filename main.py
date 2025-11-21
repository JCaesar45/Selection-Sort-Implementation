def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current element is the minimum
        min_index = i
        # Find the actual minimum element in the remaining unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
