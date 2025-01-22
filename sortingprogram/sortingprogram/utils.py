# utils.py

import numpy as np
from matplotlib import pyplot as plt

def create_array():
    array = np.random.randint(1, 100, 10)

    return array

def plot_graph(array, first_bar_index=-1, second_bar_index=-1, third_bar_index=-1, start=False, finish=False):
    if start:
        plt.ion()

    plt.clf()
    graph = plt.bar(list(range(1, len(array)+1)), array)

    if 0 <= first_bar_index < len(array):
        graph[first_bar_index].set_color("red")

    if 0 <= second_bar_index < len(array):
        graph[second_bar_index].set_color("red")

    if 0 <= third_bar_index < len(array):
        graph[third_bar_index].set_color("green")

    plt.title("Sorting Program")
    plt.xlabel("Position (Ascending Order)")
    plt.ylabel("Value")
    plt.xticks(list(range(1, len(array)+1)))
    plt.yticks(array)
    plt.draw()
    plt.pause(1)

    if finish:
        plt.ioff()
        plt.show()