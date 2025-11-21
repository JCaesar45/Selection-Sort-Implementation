```markdown
# Selection Sort Implementation

This project implements the classic Selection Sort algorithm in Python. Selection sort is a straightforward sorting technique that works by repeatedly finding the smallest element in the unsorted portion of a list and swapping it with the first unsorted element, progressively sorting the list from smallest to largest.

## Objective

Create a function named `selection_sort` that sorts a list of numbers in place without using Python's built-in `sort()` or `sorted()` functions.

## Features

- Sorts a list of numbers from smallest to largest.
- Operates in-place with constant space complexity (O(1)).
- Works efficiently with small datasets, but has quadratic time complexity O(n^2) in all cases.

## User Stories

- Define a function `selection_sort` with one parameter (the list to sort).
- Sort the list in-place without using built-in sorting methods.
- Return the sorted list for convenience.
- Handle any list of numbers correctly.

## Usage

```python
# Example usage:
numbers = [33, 1, 89, 2, 67, 245]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)  # Output: [1, 2, 33, 67, 89, 245]
``

## Implementation

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
``

## Testing

The function has been tested with multiple cases to ensure correctness:

```python
assert selection_sort([33, 1, 89, 2, 67, 245]) == [1, 2, 33, 67, 89, 245]
assert selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]) == [3, 5, 12, 15, 16, 23, 72, 99, 567]
assert selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]) == [1, 1, 2, 2, 4, 8, 32, 43, 43, 55, 63, 92, 123, 123, 234, 345, 5643]
``

## License

This project is for educational purposes. Feel free to use and modify the code as needed.
