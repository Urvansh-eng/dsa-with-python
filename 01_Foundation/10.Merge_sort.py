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
