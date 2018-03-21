from random import randint


def randomized_quicksort(array):
    inplace_randomized_quicksort(array, 0, len(array) - 1)
    return array

def inplace_randomized_quicksort(array, start, end):
    if start >= end:
        return
    lptr = start
    rptr = end - 1
    pivot_index = randint(start, end)
    array[pivot_index], array[end] = array[end], array[pivot_index]
    pivot = array[end]
    while lptr <= rptr:
        while lptr <= rptr and array[lptr] <= pivot:
            lptr += 1
        while rptr >= lptr and array[rptr] >= pivot:
            rptr -= 1
        if lptr < rptr:
            array[lptr], array[rptr] = array[rptr], array[lptr]
    array[lptr], array[end] = array[end], array[lptr]
    inplace_randomized_quicksort(array, start, lptr - 1)
    inplace_randomized_quicksort(array, lptr + 1, end)
