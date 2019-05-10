Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O(1).  We're simply re-assigning to an index of a list.

2. What is the space complexity of your ring buffer's `append` function?

O(1).  No additional memory or data structures used.

3. What is the runtime complexity of your ring buffer's `get` method?

O(n).  Have to check each value in buffer during the list comprehension.

4. What is the space complexity of your ring buffer's `get` method?

O(n).  Creating a list comprehension will take up additional memory up to a worst case of O(n) if self.storage has no 'None' values.


5. What is the runtime complexity of the provided code in `names.py`?

O(n^2).  Nested for loops will run j times for each i, so n^2.

6. What is the space complexity of the provided code in `names.py`?

O(n).  Worst case, duplicates will be a list of n-length.

7. What is the runtime complexity of your optimized code in `names.py`?

O(n).  For the hash table solution, the time complexity is dominated by the dict creation which happens in a for loop with n-iterations.  The actualy searching in the hash table is an O(1) operation.  Finally, the duplicates.append() is also O(1)

8. What is the space complexity of your optimized code in `names.py`?

O(2n) = O(n).  Creating a dictionary and a duplictes list of worst case n-length.
