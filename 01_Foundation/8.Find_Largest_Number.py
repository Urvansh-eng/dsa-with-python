# Find Largest Number

# Given an array arr of numbers, return the largest number in the array. If the array is empty, return None (Python equivalent of null).

# Approach:
# 1. Check if the array is empty.
#    - If the array is empty, print None.

# 2. Otherwise, assume the first element is the largest element.

# 3. Traverse the entire array using a loop.

# 4. Compare each element with the current largest element.
#    - If the current element is largest,
#      update the largest element.

# 5. After traversing the array,
#    print the largest element.

# Time Complexity: O(n)
# Space Complexity: O(1)



arr = [23,43,1,43,55,98]

if len(arr) == 0:
    print(0)
else:
    largest = arr[0]

    for num in arr:
        if largest < num:
            largest = num
    print(largest)    




