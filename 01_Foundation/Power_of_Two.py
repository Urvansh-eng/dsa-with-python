# Power of Two
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.



# Approach
# 1. Check if the number is less than or equal to 0. If yes, return False because powers of 2 are always positive.
# 2. Repeatedly divide the number by 2 while it is evenly divisible by 2.
# 3. After the loop, if the remaining value is 1, the original number is a power of 2.
# 4. Otherwise, it is not a power of 2.
n = 4

if n <= 0:
    print("False")
    
while n%2 == 0:
    n  = n // 2
if n == 1:
    print("True")
else: 
    print("False")
       

