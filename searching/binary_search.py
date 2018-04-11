def binary_search(array, element):
    if not array or element is None:
        return -1
    return binary_search_recursive(array, 0, len(array) - 1, element)


def binary_search_recursive(array, start, end, element):
    middle = int((end + start)/2)
    if start > end:
        return -1
    if array[middle] == element:
        return middle
    elif array[middle] < element:
        return binary_search_recursive(array, middle + 1, end, element)
    elif array[middle] > element:
        return binary_search_recursive(array, start, middle - 1, element)
