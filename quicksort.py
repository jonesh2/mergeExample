
def quickSort(aList):

def partition(list, start, end):
    pivot = list[end]                          # Partition around the last value
    bottom = start-1                           # Start outside the area to be partitioned
    top = end                                  # Ditto

    done = 0

        
    list[top] = pivot                          # Put the pivot in its place.
    return top                                 # Return the split point


def main():
    myList = [3, 2, 5, 1, 9, 0, 0, 4, 45, 12]
    quickSort(myList)
    print(myList)
