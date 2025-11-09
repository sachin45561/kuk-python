# Insertion Sort in Python

def insertion_sort(arr):
    if len(arr) <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]          # Element to be positioned
        j = i - 1 # Index of the previous element of sorted part
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] # Shift elements to the right
            j -= 1
        arr[j + 1] = key # Insert the key in the correct position

# Example usage
numbers = [9, 5, 1, 4, 3]
print("Before sorting:", numbers)

insertion_sort(numbers)
print("After sorting: ", numbers)