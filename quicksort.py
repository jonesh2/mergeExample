
def quickSort(aList):
    quickSortHelper(aList, 0, len(aList))

def quickSortHelper(aList, start, end):

def partition(list, start, end):
    pivot = list[end]                          # Partition around the last value
    bottom = start-1                           # Start outside the area to be partitioned
    top = end                                  # Ditto

    done = 0
    while not done:                        # Until we find an out of place element...
        top = top-1                        # ... move the top down.

        if top == bottom:                  # If we hit the bottom...
            done = 1                       # ... we are done.
            break

        if list[top] < pivot:              # Is the top out of place?
            list[bottom] = list[top]       # Then put it at the bottom...
            break                          # ...and start searching from the bottom.


    list[top] = pivot                          # Put the pivot in its place.
    return top                                 # Return the split point


def main():
    myList = [3, 2, 33, 1, 9, 90, 0, 5, 31, 12]
    quickSort(myList)
    print(myList)
