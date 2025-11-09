# """Write a Python program to implement the Selection Sort algorithm 
# that sorts a list of numbers."""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        print("i",i)
        min_index = i
        for j in range(i + 1, n):
            print("j",j)
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)
    return arr


# list_to_sort = [64, 25, 12, 22, 11]
list_to_sort = []
num_elements = int(input("Enter the number of elements in the list: "))
for x in range(num_elements):
    element = int(input("Enter element: "))
    list_to_sort.append(element)

sorted_list = selection_sort(list_to_sort)
print("Sorted array:", sorted_list)

