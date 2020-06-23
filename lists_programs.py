# list1 = [int,"hello",4,5,8,45,3,9,4,5,2,5,22,44,56,48,63,4]
# for item in list1:
#     if str(item).isnumeric() and item >= 6:
#         print(item)
#
#
# print(list1)


# ===============split method==========
# ========Convert string to list=======
# name = 'ASep 24'
# print(name.split())   ## ['ASep', '24']


# ======================================


# ==========join method==============
# ========Convert list to string=======

# name = ['asep','42']
# print(','.join(name))       #asep,42


# =======================pop()============

# fruits3 = ['banana', 'kiwi', 'apple', 'mangoes']
# print(fruits3.pop())     #mangoes
# print(fruits3)            #['banana', 'kiwi', 'apple']

# ===========================================
# ==========Index Method ============
# numbers = [1,2,3,4,5,6,7,8,9,1,5]
# print(numbers.index(4))    #3
# print(numbers.index(4,1,5))

# =========== [is V/S ==]  ------------
# fruits1 = ['orange', 'apple', 'pear']
# fruits2 = ['orange', 'apple', 'pear']
# fruits3 = ['banana', 'kiwi', 'apple', 'banana']
#
# print(fruits1 == fruits2)   # True [checks only elements]values are same
# print(fruits1 is fruits2)   # False [checks memory for ellement]][ Different memory location]


# =======================================
# ======================================
#
# ===========Sublist-==================
#
# list1 = [[1,2,3],[4,5,6],[7,8,9]]   #2d list
# for sublist in list1:
#     for i in sublist:
#         print(i , end=" ")   #1 2 3 4 5 6 7 8 9


# ===================================
# ==========List inside list=========

# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 2d list
# print(list1[0][0]) #1
# print(list1[0][1]) #2
# print(list1[0][2]) #3
# # =====================
# print(list1[1][0]) #4
# print(list1[1][1]) #5
# print(list1[1][2]) #6
# # =======================
# print(list1[2][0]) #7
# print(list1[2][1]) #8
# print(list1[2][2]) #9


# =======================================
# ====== Auto list making ===============

# numbers = list(range(1,10))
# print(numbers)

# ==============================
# =============negetive list to function========
# number = [1,2,3,4,5,6,7,8,9,10]
# def negetive_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative
#
# print(negetive_list(number))

# =========================================
# ===== Square of values in list

# numbers = [1,2,3,4]
# numbers = list(range(1,21))
# def square_of(l):
#     square = []
#     for i in l:
#         square.append(i*i)
#     return square
#
# print(square_of(numbers))


# =========================================
# ====== Reverse without slicing / reverse ==
# def use_reverse(l):  # reverse
#     l.reverse()
#     return l
#
#
# def use_slicing(l):  # Slicing
#     return l[::-1]
#
#
# # numbers = str(numbers)
# def reverse_word(l):    # User defined function
#     revers = []
#     # for i in l:
#     for i in range(len(l)):
#         revers.append(l.pop())
#     return revers
#
#
# numbers = [1, 2, 3, 4, 5]
# # print(use_reverse(numbers))
# # print(use_slicing(numbers))
# print(reverse_word(numbers))
#

# =====================================
# ===== list[values] reverse ===========

# lenth_of_list = len(list1)
# print(lenth_of_list)
# def reverse_list_value(l):
#     r_list = []
#     # for i in range(len(l)):
#         # r_list.append(l.pop())    #['xyz', 'pqr', 'abc']
#     for i in l:
#         r_list.append(i[::-1])   #['cba', 'rqp', 'zyx']
#     return r_list
# list1 = ['abc','pqr','xyz']
# print(reverse_list_value(list1))


print("===============================")
print("========List comprehensive=======")
print("")
# negetaive = []
# for i in range(1,11):
#     negetaive.append(i)
#     # print(i)
# # print(negetaive)
#
# negetaive1 = [i for i in range(1,110) ]
# print(negetaive1)


# list1 = ['Asep', 'Mannan', 'Sayyad']
# print(list1)
# filtered = []
# for name in list1:
#     filtered.append(name[0])
#
# print(filtered)  # ['A', 'M', 'S']
#
# short_filter = [name[0] for name in list1]
# print(short_filter)  # ['A', 'M', 'S']


# =========================If statement======

numbers = list(range(1, 11))
print(numbers)

# even_nums = [ i for i in numbers if i%2==0]
# print(even_nums)


# ============ if else ==========
new_list = []
for i in numbers:
    if i % 2 == 0:
        new_list.append(i * 2)
    else:
        new_list.append(-i)
print(new_list)  # [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]

# ============== Short====

new_list = [i * 2 if (i % 2 == 0) else -i for i in numbers]
print(new_list)  # #[-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]
