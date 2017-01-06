quickSort(aList, start, end)
    if start < end:                            # If there are two or more elements...
        split = partition(aList, start, end)    # ... partition the sublist...
        quicksort(aList, start, split-1)        # ... and sort both halves.
        quicksort(aList, split+1, end)
    else:
        return


def main():
    myList = [3, 2, 5, 1, 9, 0, 0, 4, 45, 12]
    quickSort(myList, 0, len(myList))
    print(myList)
