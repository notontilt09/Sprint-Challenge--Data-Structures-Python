import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
"""
Below is original implementation with nested for loop and O(n^2) runtime
"""
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

"""
Below is for loop with a nested BST which is O(n log(n)) runtime
"""
# # initialize bst with first name
# bst = BinarySearchTree(names_1[0])
# # append all other names in first file to bst
# for i in names_1[1:]:
#     bst.insert(i)

# # loop through names_2 and if bst contains the name, append to duplicates
# for j in names_2:
#     if bst.contains(j):
#         duplicates.append(j)

"""
Below is hash table to try and get runtime to O(2n) = O(n)
"""
# # initialize hash table
# lookup = {}

# # loop through names1 and add keys to hash table for each name.  Value is irrelevant, we just care about the keys.
# for i in names_1:
#     lookup[i] = 1

# for j in names_2:
#     if j in lookup.keys():
#         duplicates.append(j)


"""
Stretch:  Can only use lists
"""
# This is about 5x faster than original solution.  I'm guessing because the nested loop is python optimized search.
# for i in names_1:
#     if i in names_2:
#         duplicates.append(i)


# I think a faster way might be sorting one of the lists, then performing binary search for each name in 2nd list.
# Should be O(n log(n)) if done correctly
sorted_1 = sorted(names_1)

def search(value, arr, left, right):
    # binary search algo
    if left > right:
        return None
    midpoint = left + (right - left) // 2
    if arr[midpoint] == value:
        return value
    elif arr[midpoint] > value:
        return search(value, arr, left, midpoint - 1)
    elif arr[midpoint] < value:
        return search(value, arr, midpoint + 1, right)

for i in names_2:
    if search(i, sorted_1, 0, len(sorted_1) - 1) is not None:
        duplicates.append(i)
    



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

