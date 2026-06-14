# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

# An alphanumeric string is a string consisting of lowercase English letters and digits.

alpha = "a1b5c3d5e9"
digits = []

for letter in alpha:
    if letter.isdigit():
        digits.append(letter)
    
   
# unique = set(digits)
# unique_list = list(unique)
# unique_list.sort()
sorted_digits = sorted(set(digits))
# print(sorted_digits)
if len(sorted_digits) <= 1:
    print(-1)
else:
    second_largest = sorted_digits[-2]
    print(f"second largest element is {second_largest}")