#Linked list implementation in Python
# Sorting
# """
#   1. Bubble Sort
#   2. Insertion Sort
#   3. Selection Sort
#   4. Quick Sort
#   5.  Merge Sort
#   6. Heap Sort
# """

# Search Algorithms
# 1 . Linear Search: """
# For unsorted and unordered small lists
# """
# 2. Binary Search

# LINEAR SEARCH
def linearSearch(values, target):
    """
    LinearSearch algorithm..
    Values = An array with all the values
    Target = Value to be found in the algorithm
    """
    for i in values:
        if i == target:
            print (f'{i}, Index:{values.index(i)}')
        print("Not Found")



values = [2,3,23,1,4,12,4,2,9,288,283]
linearSearch(values, 12)


# BINARY SEARCH
# 1. Start at the middle element:
# 2. If the target value is equal to the middle element of the array then return the index of the element
# 3. If target value is greater than  middle element , pick the elements to the right and start with step 1
# 4. If target value is less than  middle element , pick the elements to the left and start with step 1
# 5. When the item is found return the index of the matched element
#  6. If no match return not found/ -1

def binarySearch(values, target, length):
    """
    Binary: List to be searched
    Target:  Search Term
    len: The number of elements in the list
    """
    max = (length - 1)
    min = 0
    step = 0
    
    for number in values:
        while max >= min :
            center = (max + min ) / 2
            # step = 0
            step += 1
            if values[center] == target:
                print(values[center])
                # return step
            elif values[center] > target:
                max = (center - 1)
            min = (center + 1 )

listt  = [1,3,5,7,9,2,39,33,2]
size = len(listt)
binarySearch(listt, 39, size)