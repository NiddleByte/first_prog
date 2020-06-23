# dict1 = {
#     'name' : 'Asep',
#     'age' : 24,
#     'fav_movie': 'coco',
#     'fav_song': 'sorry'
# }
# print(dict1)
#
# # dict1.pop('name')
# dict1.popitem()
# # print(dict1)
# print(dict1)
# print(type(dict1))
# print(dict1)
#
# if 'Asep' in dict1.values():
#     print("present")
# else:
#     print("Not present")
#
# for i in dict1.values():
#     print(i)
#
# for i, j in dict1.items():
#     print(f"{i} :: {j}")


# d = dict1.fromkeys(['name','age','fav_movie'],'unknown')
# print(d)
#
# d = dict1.fromkeys("abcde",'uknown')
# print(d) #{'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}


# =======================
# ===== Get() Method========

# print(dict1['name'])

# print(dict1.get('names')) ## none     #names is not in dictionary
# print(dict1.get('name'))  ## asep     #name is present


# ========== Cube Finder ============

# def cube_find(n):
#     dict1={}
#     for i in range(1,n+1):
#         dict1[i]=i**3
#         print(i ,":", dict1[i])
#     return dict1
# # n = int(input("Enter your number for cube"))
# print(cube_find(4))
# # cube_find(n)

# ======== Word Counter =============
# def word_counter(s):
#     count = {}
#     for char in s:
#         count[char] = s.count(char)
#         print(char)
#     return  count
#
# s = input("Enter Name")
# print(word_counter(s))
