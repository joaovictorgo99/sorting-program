# sort.py

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def selection_sort(array):
    for i in range(len(array)):
        minimum_value_index = i

        for j in range(i+1, len(array)):
            if array[j] < array[minimum_value_index]:
                minimum_value_index = j
                
        array[i], array[minimum_value_index] = array[minimum_value_index], array[i]

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i-1
        value = array[i]

        while j >= 0 and array[j] > value:
            array[j+1] = array[j]
            j = j-1

        array[j+1] = value

def shell_sort(array):
    gap = len(array)//2

    while gap >= 1:
        for i in range(gap, len(array)):
            j = i
            value = array[i]

            while j >= gap and array[j-gap] > value:
                array[j] = array[j-gap]
                j = j-gap

            array[j] = value

        gap = gap//2

def quick_sort(array):
    if len(array) <= 1:  # Base case
        return array
    else:  # Recursive case
        j = 1
        pivot = array[0]

        for i in range(1, len(array)):
            if array[i] <= pivot:
                array[i], array[j] = array[j], array[i]
                j = j+1

        array[0], array[j-1] = array[j-1], array[0]

        quick_sort(array[:j-1])
        quick_sort(array[j:])

        return array

def merge_sort(array):
    if len(array) <= 1:  # Base case
        return array
    else:  # Recursive case
        mid = len(array)//2
        i = 0
        j = mid
        ordered_array = []

        merge_sort(array[:mid])
        merge_sort(array[mid:])

        while i < len(array)//2 and j < len(array):
            if array[i] <= array[j]:
                ordered_array.append(array[i])
                i = i+1
            else:
                ordered_array.append(array[j])
                j = j+1

        while i < len(array)//2:
            ordered_array.append(array[i])
            i = i+1

        while j < len(array):
            ordered_array.append(array[j])
            j = j+1

        for k in range(len(array)):
            array[k] = ordered_array[k]

        return array

def heap_sort(array):
    if len(array) <= 1:  # Base case
        return array
    else:  # Recursive case
        i = len(array)

        while i > 1:
            i = i-1
            j = (i-1) // 2

            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

        array[0], array[len(array)-1] = array[len(array)-1], array[0]

    heap_sort(array[:-1])

    return array