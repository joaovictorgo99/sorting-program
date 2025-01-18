# menu.py

from matplotlib import pyplot as plt
import sort
import utils

def call_menu():
    print(f"SORTING PROGRAM")
    print(f"Welcome user, please select one of the sorting algorithms below.")
    print(f"[1] Bubble Sort;")
    print(f"[2] Selection Sort;")
    print(f"[3] Insertion Sort;")
    print(f"[4] Shell Sort;")
    print(f"[5] Quick Sort;")
    print(f"[6] Merge Sort;")
    print(f"[7] Heap Sort;")
    print(f"[0] Exit.")

    select_algorithm()

    print(f"Goodbye user!")

def select_algorithm():
    option = -1

    while option != 0:
        try:
            option = int(input(f"Option: "))
        except ValueError:
            print(f"This is not a valid option.")

        array = utils.create_array()

        if option == 1:
            sort.bubble_sort(array)
        elif option == 2:
            sort.selection_sort(array)
        elif option == 3:
            sort.insertion_sort(array)
        elif option == 4:
            sort.shell_sort(array)
        elif option == 5:
            sort.quick_sort(array)
        elif option == 6:
            sort.merge_sort(array)
        elif option == 7:
            sort.heap_sort(array)
        elif option == 0:
            break
