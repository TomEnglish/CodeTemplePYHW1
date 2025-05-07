
# Challenge: You are given a list of numbers. 
# The numbers each repeat a certain number of times. 
# Remove all numbers that repeat an odd number of times 
# while keeping everything else the same.

 # Solution:
def odd_ones_out(numbers):
    keepers = []
    for i in numbers:
        count = numbers.count(i)
        # print(i, count)
        if count % 2 == 0:
            keepers.append(i)
    return keepers

# x = [1, 1, 2, 2, 3, 3, 3]
# y = [26, 23, 24, 17, 23, 24, 23, 26]
# z = [1, 2, 3]
# a = [1]
# print(odd_ones_out(x))
# print(odd_ones_out(y))
# print(odd_ones_out(z))
# print(odd_ones_out(a))


# We need a function that can transform a number (integer) into a string.


# Solution:
def string_to_number(num):
    num_str = str(num)
    return num_str

# print(type(string_to_number(123)))
# print(string_to_number(123))
# print(type(string_to_number(999)))
# print(string_to_number(999))
# print(type(string_to_number(-100)))
# print(string_to_number(-100))

# Write a function that removes the spaces from the string, then return the resultant string.

 # Solution:
def no_space(x):
    return x.replace(" ","")

# w = "8 j 8   mBliB8g  imjB8B8  jl  B" 
# y =  "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"
# z = "8aaaaa dddd r     "

# print(no_space(w))
# print(no_space(y))
# print(no_space(z))

# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

 # Solution:
def is_vow(x):
    y = []
    vowels = ['a','e','i','o','u']
    ascii_vowels = list(map(ord,vowels))
    for i in range(len(x)):
        if x[i] in ascii_vowels:
            y.append(chr(x[i]))
        else:
            y.append(x[i])
    return y
 