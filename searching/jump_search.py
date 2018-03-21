import math


def jump_search(array, element):
    if not array or not element:
        return -1
    n = len(array)
    interval = int(math.sqrt(n))
    pointer = 0
    for i in range(0, n, interval):
        if array[i] < element:
            pointer = i
        elif array[i] == element:
            return i
        else:
            break
    for j in range(pointer, pointer + interval):
        if array[j] == element:
            return j
    return -1
