# The town sheriff dislikes odd numbers and wants all odd numbered families out of town! In town crowds can form and individuals are often mixed with other people and families. However you can distinguish the family they belong to by the number on the shirts they wear. 
# As the sheriff's assistant it's your job to find all the odd numbered families and remove them from the town!

# Challenge: You are given a list of numbers. The numbers each repeat a certain number of times. Remove all numbers that repeat an odd number of times while keeping everything else the same.

# odd_ones_out([1, 2, 3, 1, 3, 3]) = [1, 1]
# In the above example:

# the number 1 appears twice
# the number 2 appears once
# the number 3 appears three times
# 2 and 3 both appear an odd number of times, so they are removed from the list. The final result is: [1,1]

# Here are more examples:

# odd_ones_out([1, 1, 2, 2, 3, 3, 3]) = [1, 1, 2, 2]
# odd_ones_out([26, 23, 24, 17, 23, 24, 23, 26]) = [26, 24, 24, 26]
# odd_ones_out([1, 2, 3]) = []
# odd_ones_out([1]) = []
# Are you up to the challenge?
# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(odd_ones_out([1,2,3,1,3,3]), [1,1])
#         test.assert_equals(odd_ones_out([75, 68, 75, 47, 68]), [75, 68, 75, 68])
#         test.assert_equals(odd_ones_out([42, 72, 32, 4, 94, 82, 67, 67]), [67, 67])
#         test.assert_equals(odd_ones_out([100, 100, 5, 5, 100, 50, 68, 50, 68, 50, 68, 5, 100]), [100, 100, 100, 100])
#         test.assert_equals(odd_ones_out([82, 86, 71, 58, 44, 79, 50, 44, 79, 67, 82, 82, 55, 50]), [44, 79, 50, 44, 79, 50])

# def odd_ones_out(numbers):
#     keepers = []
#     for i in numbers:
#         count = numbers.count(i)
#         # print(i, count)
#         if count % 2 == 0:
#             keepers.append(i)
#     return keepers

# x = [1, 1, 2, 2, 3, 3, 3]
# y = [26, 23, 24, 17, 23, 24, 23, 26]
# z = [1, 2, 3]
# a = [1]
# print(odd_ones_out(x))
# print(odd_ones_out(y))
# print(odd_ones_out(z))
# print(odd_ones_out(a))
# Note: This kata is inspired by Convert a Number to a String!. Try that one too.

# Description
# We need a function that can transform a string into a number. What ways of achieving this do you know?

# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

# Examples
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7
#         test.assert_equals(string_to_number("1234"), 1234)
#         test.assert_equals(string_to_number("605"), 605)
#         test.assert_equals(string_to_number("1405"), 1405)
#         test.assert_equals(string_to_number("-7"), -7)

# Description:
# We need a function that can transform a number (integer) into a string.

# What ways of achieving this do you know?

# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

# def string_to_number(num):
#     num_str = str(num)
#     return num_str

# print(type(string_to_number(123)))
# print(string_to_number(123))
# print(type(string_to_number(999)))
# print(string_to_number(999))
# print(type(string_to_number(-100)))
# print(string_to_number(-100))

# Write a function that removes the spaces from the string, then return the resultant string.

# Examples (Input -> Output):

# "8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
# "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
# "8aaaaa dddd r     " -> "8aaaaaddddr"

# def no_space(x):
#     return x.replace(" ","")

# w = "8 j 8   mBliB8g  imjB8B8  jl  B" 
# y =  "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"
# z = "8aaaaa dddd r     "

# print(no_space(w))
# print(no_space(y))
# print(no_space(z))

# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

# If they are, change the array value to a string of that vowel.

# Return the resulting array.

    #  ([118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ], [118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ]),
    #         (["e",121,110,113,113,103,121,121,"e",107,103 ], [101,121,110,113,113,103,121,121,101,107,103 ]),
    #         ([118,103,110,109,104,106 ], [118,103,110,109,104,106 ]),
    #         ([107,99,110,107,118,106,112,102 ], [107,99,110,107,118,106,112,102 ]),
    #         ([100,100,116,"i","u",121 ], [100,100,116,105,117,121 ]),

vowels = ['a','e','i','o','u']
ascii_vowels = list(map(ord,vowels))
print(ascii_vowels)
test = [97, 98, 99, 101]

def switch_vowels(x):
    y = []
    for i in range(len(x)):
        if x[i] in ascii_vowels:
            y.append(chr(x[i]))
        else:
            y.append(x[i])
    return y


print(switch_vowels(ascii_vowels))
print(switch_vowels(test))  