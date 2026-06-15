# Given an array of numbers, return the smallest number.
# If the array is empty, return None (Python equivalent of null).


# Approach:

# 1. Check if the array is empty.
#    - If the array is empty, print None.

# 2. Otherwise, assume the first element is the smallest element.

# 3. Traverse the entire array using a loop.

# 4. Compare each element with the current smallest element.
#    - If the current element is smaller,
#      update the smallest element.

# 5. After traversing the array,
#    print the smallest element.

# Time Complexity: O(n)
# Space Complexity: O(1)



arr = []

if len(arr) == 0:
    print(None)
else:
    smallest = arr[0]

    for num in arr:
        if smallest > num: 
            smallest = num
    print(smallest)                    
      
              




