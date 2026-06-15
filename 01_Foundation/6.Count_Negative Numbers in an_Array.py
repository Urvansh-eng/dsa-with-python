# Count Negative Numbers in an Array

# Approach:
# 1. Take an array of numbers.
# 2. Create a new list containing only the negative numbers
#    using list comprehension.
# 3. Count the number of elements in the new list using len().
# 4. Print the count.

# Time Complexity: O(n)
# Space Complexity: O(n)

x =[-1,-2,-3,4,-5]

negative_list = [num for num in x if num<0]


negative_numbers = len(negative_list)
print(negative_numbers)


#2nd method

# Approach:
# 1. Initialize count = 0.
# 2. Traverse each element in the array.
# 3. If the element is less than 0, increment count.
# 4. After traversal, return/print count.

# Time Complexity: O(n)
# Space Complexity: O(1)



# x = [-1, -2, -3, 4, -5]

# count = 0

# for num in x:
#     if num < 0:
#         count += 1

# print(count)