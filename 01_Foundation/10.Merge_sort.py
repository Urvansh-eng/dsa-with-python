# Sort an Array
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# nums = [1,4,3,2,7,6,8]




# def merge(nums,l,m,h):
#     i = 0
#     j = 0
#     arr =[]
#     left = nums[1:m+1]
#     right = nums[m+1:h+1]
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             arr.append(left[i])
#             i+=1
#         else:
#             arr.append(right[j])
#             j += 1
#     while i< len(left):
#         arr.append(left[i])
#         i += 1
#     while j < len(right):
#         arr.append(right[j])
#         j += 1
#     nums[l:h+1] = arr

 
        

    

# def MergeSort(nums,l,h):
#     if l >=h:
#         return
#     m = (l + h)//2
#     MergeSort(nums,l,m)
#     MergeSort(nums,m+1,h)
#     merge(nums,l,m,h)




# Approach:
# 1. If the array has 0 or 1 element, it is already sorted, so return it.
# 2. Find the middle index and divide the array into left and right halves.
# 3. Recursively apply merge sort on both halves until each subarray contains a single element.
# 4. Merge the two sorted halves by comparing their elements one by one.
# 5. Add the smaller element to a new list and move its pointer forward.
# 6. After one half is exhausted, append the remaining elements from the other half.
# 7. Return the merged sorted list as the final result.





arr = [1,3,2,5,4,7,6,0,9,8]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left,right):
    i = 0
    j = 0
    new = []
    while i< len(left) and j<len(right):
        if left[i] <= right[j]:
            new.append(left[i]) 
            i += 1
        else:
            new.append(right[j]) 
            j += 1
           

    while i < len(left):
        new.append(left[i])
        i += 1
    while j < len(right):
        new.append(right[j])
        j += 1
    return new
    


result = merge_sort(arr)
print(result)
