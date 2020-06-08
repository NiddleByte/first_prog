# name = input("Enter your name")
#
# print(f"Your name {name[::-1]}")


# ==========Exercise 2=======
# ==== Solution on spaces==========
#
# name , word = input("Enter name and single word with comma separated ").split(",")
# # name_tmp = name.lower()
# # word_tmp = word.lower()
# # print("Total Words are",len(name_tmp),end="\n")
# # print("Searched words ",name_tmp.count(word_tmp))
#
# name_strp = name.replace(" ","").lower()
# word_strp = word.strip().lower()
#
# print(len(name_strp),end=" \n")
# print(name_strp.count(word_strp),end=" ")


# ========= Center method ============

# name = "Asep"
# print(name.center(6,"*"))      # *Asep*


# =========== Center Method Auto detect len ===========
#
# name = input("Enter Your text")                     # Asep Mannan Sayyad
# star = input("Enter Your Symbolic Character")       # +
# lenth_word  =  int(input("Enter Lenth "))           # 6
# # char_len = len( star)
# # single_char = star[0]
# lenth = len(name) + lenth_word*2
# #we can also replace the spaces with char
# print(name.center(lenth, star))       #++++++Asep Mannan Sayyad++++++
#
# tmp = name.center(lenth, star)
# print()
# print(tmp.replace(" ", star))       #++++++Asep+Mannan+Sayyad++++++


# ==================== Find word and count the repeated words ==============

# str = input("Enter Your Name")
# tmp = "Asep Sayyad "                  # AsepSayyad
# print(f"Your Name is: {tmp}")       #
# str = tmp.lower()                   # asepsayyad
# loops = len(str)                    # 10
# # # print(loops)
# i = 0
# j = 0
# tmp1 = str.count("a")
# print(tmp[0] , tmp.count("a"))
# temp = ""
# while i < loops:
#    if str[i] not in temp:
#     temp + str[i]
#     print(f"{str[i]}:{str.count(str[i])}")
#    i += 1
#

# ============ using for loop =============
# name = input("Enter your name")
# temp = ""
# for i in range (len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]}: {name.count(name[i])}")
#         temp +=name[i]

# =======================Palindrome-=============

def is_palindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    return False

print(is_palindrome("155000"))
print(is_palindrome("1.(11(11(.1"))