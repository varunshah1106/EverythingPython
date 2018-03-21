def interpolation_search(array, element):
    if not array or not element:
        return -1
    start = 0
    end = len(array) - 1
    while array[start] <= element <= array[end]:
        slope = (end - start)/(array[end] - array[start])
        middle = int(start + (element - array[start]) * slope)
        if array[middle] < element:
            start = middle + 1
        elif array[middle] > element:
            end = middle - 1
        else:
            return middle
    if array[start] == element:
        return start
    return -1
