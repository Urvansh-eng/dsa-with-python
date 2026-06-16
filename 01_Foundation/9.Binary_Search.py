# Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


arr = [1,2,3,4,5,6]

left = arr[0]
right = arr[len(arr) - 1]
target = 1

while left <= right:
    middle = ((left+right) // 2)
    if middle == target:
        print(middle)
        break

    elif target < middle:
        right = middle - 1
    else:
        left = middle  + 1
    
else:
    print(-1)