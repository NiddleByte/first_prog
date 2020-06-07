# name = input("Enter your name")
#
# print(f"Your name {name[::-1]}")


# ==========Exercise 2=======
#==== Solution on spaces==========
#
name , word = input("Enter name and single word with comma separated ").split(",")
# name_tmp = name.lower()
# word_tmp = word.lower()
# print("Total Words are",len(name_tmp),end="\n")
# print("Searched words ",name_tmp.count(word_tmp))

name_strp = name.replace(" ","").lower()
word_strp = word.strip().lower()

print(len(name_strp),end=" \n")
print(name_strp.count(word_strp),end=" ")