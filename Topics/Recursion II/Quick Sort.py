def quicksort(lst):
    """
        Sorts an array in the ascending order in O(n log n) time
        :param lst: a list of numbers
        :return: the sorted list
    """
    n = len(lst)
    qsort(lst, 0, n - 1)


def qsort(lst, low, high):
    """
        Helper
        :param lst: the list to sort
        :param low:  the index of the first element in the list
        :param high:  the index of the last element in the list
        :return: the sorted list
    """
    if low < high:
        p = partition(lst, low, high)
        qsort(lst, low, p - 1)
        qsort(lst, p + 1, high)


def partition(lst, low, high):
    """
        Picks the last element hi as a pivot
         and returns the index of pivot value in the sorted array
    """
    pivot = lst[high]
    i = low
    for j in range(low, high):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[i], lst[high] = lst[high], lst[i]
    return i
