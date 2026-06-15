# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

x = -120

is_negative = x < 0


x = list(str(abs(x)))
# x = str(x)
# y = list(x)




new_list = []

while x:
    new_list.append(x.pop())
    


reversed_list = int("".join(new_list))
# print(type(new_list))

if is_negative:
    reversed_list = -1 * reversed_list

# print(reversed_list)    
    
if -2147483648 <= reversed_list <= 2147483647:
    print(reversed_list)
else:
    print(0)