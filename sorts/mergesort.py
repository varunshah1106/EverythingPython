def mergesort(array):
    if len(array) < 2:
        return array
    middle = int(len(array)/2)
    return merge(mergesort(array[:middle]), mergesort(array[middle:]))

def merge(left, right):
    combined = []
    l = len(left)
    r = len(right)
    i = j = 0
    while i < l and j < r:
        if left[i] <= right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1
    combined += left[i:] or right[j:]
    return combined
