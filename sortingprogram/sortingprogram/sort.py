# sort.py

import utils

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            utils.plot_graph(array, j)

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def selection_sort(array):
    for i in range(len(array)):
        minimum_value_index = i

        for j in range(i+1, len(array)):
            utils.plot_graph(array, minimum_value_index, j)

            if array[j] < array[minimum_value_index]:
                minimum_value_index = j

                utils.plot_graph(array, minimum_value_index, j)
                
        array[i], array[minimum_value_index] = array[minimum_value_index], array[i]

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i-1
        value = array[i]

        while j >= 0 and array[j] > value:
            utils.plot_graph(array, j, j+1 ,i)

            array[j+1] = array[j]
            j = j-1

        array[j+1] = value

        utils.plot_graph(array, j, j+1, i)

def shell_sort(array):
    gap = len(array)//2

    while gap >= 1:
        for i in range(gap, len(array)):
            j = i
            value = array[i]

            while j >= gap and array[j-gap] > value:
                utils.plot_graph(array, j, j-gap)

                array[j] = array[j-gap]
                j = j-gap

            array[j] = value

            utils.plot_graph(array, j, j-gap)

        gap = gap//2

def quick_sort(array):
    if len(array) <= 1:  # Base case
        return array
    else:  # Recursive case
        j = 1
        pivot = array[0]

        for i in range(1, len(array)):
            utils.plot_graph(array, 0, i, j)

            if array[i] <= pivot:
                array[i], array[j] = array[j], array[i]
                j = j+1

                utils.plot_graph(array, 0, i, j)

        array[0], array[j-1] = array[j-1], array[0]

        utils.plot_graph(array, 0, j-1, j)

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

        utils.plot_graph(array, third_bar_index = j)

        merge_sort(array[:mid])
        merge_sort(array[mid:])

        while i < len(array)//2 and j < len(array):
            utils.plot_graph(array, i, j)

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

            utils.plot_graph(array, k)

        return array

def heap_sort(array):
    if len(array) <= 1:  # Base case
        return array
    else:  # Recursive case
        i = len(array)

        while i > 1:
            i = i-1
            j = (i-1) // 2

            utils.plot_graph(array, i, j)

            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

                utils.plot_graph(array, i, j)

        array[0], array[len(array)-1] = array[len(array)-1], array[0]

        utils.plot_graph(array, 0, len(array)-1)

    heap_sort(array[:-1])

    return array