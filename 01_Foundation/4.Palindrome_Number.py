# Given an integer x, return true if x is a palindrome, and false otherwise.

x = 12345621
y = str(x)

is_palindrome = True

for i in range(len(y)// 2):
    if y[i] != y[-(i+1)]:
        is_palindrome = False
        False

if is_palindrome:
    print(f"{x} is plaindrome")        
else:
    print(f"{x} is not plaindrome")        

        
    
        
