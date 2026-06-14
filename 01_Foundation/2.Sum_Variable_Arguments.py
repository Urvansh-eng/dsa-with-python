# Design a function sum that can take any number of arguments and return their total.

# The function should work for both:

# Fixed number of arguments
# Variable number of arguments


def sum_num(*args):
    total = 0
    for num in args:
        total +=  num
    return total

print(sum_num(1,2,3,4,5))
print(sum_num())
print(sum_num(1))
print(sum_num(1,2))
print(sum_num(1,2,3,4,5,1,2,3,4,5))
print(sum_num(10,20,3,40,5))
