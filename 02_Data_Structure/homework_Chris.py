"""
Task3* If you have a time you can try also this:
Write a program that performs the following operations on a two-dimensional list:
(You can create your own two-dimensional list)

a) print each row of the list in the new line,
b) calculate of the sum of those elements of the list, the value of which is greater than 4, print one time at the end
this sum
c) calculate the number of elements whose value is different than 0, print one time at the end this value
d) check if the list includes an element whose value is less than 5, print bool type: True or False
"""
lst = [[5, 7, 11, 2, 3, 1],
       [4, 0, 8, 10]]

print(lst[0])


[print(lst[index_row][1]) for index_row in range(len(lst))]
for index_row in range(len(lst)):
    print(lst[index_row][1])

print(lst[0][1])
print(lst[1][1])



for i in lst:
    print(i)

big_lst = lst[0] + lst[1]
print(sum(big_lst))
some_num = 0
# some_num =+
result = sum([n for n in big_lst if n > 4])
print(f'result = {result}')
for n in big_lst:
    if n > 4: # this condition doesn't work, I don't know why
        some_num += n
print(some_num)

n_count = 0
for m in big_lst:
    if m != 0:       # this condition doesn't work either
       n_count += 1
print(n_count)
n_count = len([m for m in big_lst if m != 0])
print(n_count)



'''
Generate 20 numbers (0-19), next each even number set as a key in dictionary
and the value set as a square of the key. Print dictionary at the end.
'''

even_list = dict([(i, i**2) for i in range(0, 20) if i % 2 == 0])
print(even_list)

# Zip returns tuple
# dict_num = dict(zip(even_list, squared_list))
# print(f'dict_num {dict_num}')


"""
Write a function 'message', which takes as an argument a dictionary
with the keys:
* **name**,
* **role**,
* **movie**.

The function should return a formatted string "In _movie_, _name_ is
a _role_.", where _movie_, _name_, and _role_ is replaced with the
coresponding values from the dictionary. If any of the values is missing
from the dictionary, the function should return 'None'.
"""

cinema_dict = {
    "name": ["Sean Connery", "Jonny Deep", "Elizabeth Taylor"],
    "role": ["King Arthur", "Jack Sparrow", "Cleopatra"],
    "movie": ["First Knight", "Pirates of the Caribbean", "Cleopatra"],
    "year": ["1995", "2003", "1963"]
}

def message(some_dict):
    name_list_1, name_list_2, name_list_3 = [],[], []
    for i in some_dict.values():
        name_list_1.append(i[0])
        name_list_2.append(i[1])
        name_list_3.append(i[2])

    return f"In {name_list_1[2]}, {name_list_1[0]} is a {name_list_1[1]}.", f"In {name_list_2[2]}, {name_list_2[0]} is a {name_list_2[1]}.", f"In {name_list_3[2]}, {name_list_3[0]} is a {name_list_3[1]}."


print(message(cinema_dict))


"""
Write a program that reads a line of text, and then prints the most 
frequent letter in it. The program should ignore case ' ', and the most frequent
should be capitalized. If there is more than one letter that appears most frequently,
it is enough to print any of them (for ambitious: write all such numbers)

Tip: I suggest creating a dictionary that stores for each letter the number of 
its occurrences. The number of occurrences of a given letter can be found using the count
method for a text string 
"""

def get_most_frequent_letter(text):
    text = text.lower()
    dict_of_letters = {key: text.count(key) for key in text if key.isalpha()}
    print(f' dict: {dict_of_letters}')


get_most_frequent_letter("In First Knight")


# #Solution with lists:
#
# str_list = [i.lower() for i in input().split()]
# alpha_list = []
# dict_alpha = {}
# result = []
#
# for i in str_list:
#     for j in i:
#         if j.isalpha():
#             alpha_list.append(j)
#
# # dict_alpha.fromkeys(alpha_list)
# # print(alpha_list)
#
# for alpha in alpha_list:
#     counter = alpha_list.count(alpha)
#     if counter > 1:
#         result = [alpha, counter]
#         print(*result)


# Final version with dictionary that really works
str_list = [i.upper() for i in input().split()]
alpha_list = []
dict_alpha = {}
max_alpha = []
count_lst = []

for word in str_list:
    for alpha in word:
        if alpha.isalpha():
            alpha_list.append(alpha)
print(alpha_list)

for item in alpha_list:
    dict_alpha[item] = dict_alpha.get(item, 0) + 1

final_dict = {element: count for element, count in dict_alpha.items() if count > 1}
print(final_dict)
#In First Knight, Sean Connery is a King Arthur.



'''
Write a function dice(num), which simulates a roll with a 6-side dice. Argument num
is a number of dice to throw. The function should return the sum of the dice.
'''
import random

def dice(num):

    sum_numbers = sum([random.randint(1, 6) for _ in range(num)])
    print(f"sum of numbers: {sum_numbers}")

# 2nd solution
#sum_1 = 0
    # result = []
    # for _ in range(num):
    #     sum_1 += random.randint(1, 6)
    # return sum_1


dice(5)

"""
Using the function dice(num) from the previous exercise, write
a function 'print_histogram(throws) that rolls two dice _throws_
times and **prints** a histogram of the resulting numbers according
to the example.

 2: ##############
 3: ########################
 4: ######################################
 5: ####################################################
 6: #################################################
 7: #################################################################
 8: ###################################################
 9: #########################################
10: ###############################
11: ################
12: ##############


Please mind the formatting (e.g. every number **must** span two characters
and be right-aligned).

Shortcut of the function logic: check how many twos, threes, fourse, etc.
"""

import random

def dice(num):
    sum_numbers = sum([random.randint(1, 6) for _ in range(num)])
    return sum_numbers

def print_histogram(throws):
    hashtag = "#"
    dict_12 = {k : "" for k in range(2, 13)}
    for i in range(throws):
        result = dice(2)
        dict_12[result] += "#"
    for k, v in dict_12.items():
        print(f"{k}: {v}")


print(print_histogram(100))
