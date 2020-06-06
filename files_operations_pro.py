
# ========== Read =============

# f = open("test.txt","r")
# content = f.read()
# print(content)
# f.close()
# --------------- Readline / Readlines --------------

# f = open("test.txt","r")
# # print(f.readline()) #f.readline()
#
# # ----------------------------------------------
#
# print(f.readlines())            # text in list format
#
# # -------------------------------
# list1 = f.readlines()           # save text in list
# for items in list1:
#     print(items)

#========= Write ============
#
# f = open("test.txt","w")
# f.write(" How are you \n What are you doing")
# content = f.read()
# f.close()


#=========== Read and Write ==========
# a=input("enter")
# f = open("test.txt","r+")
# content = f.read()      ####  Here program saves existing file data
# # print(content)
# f.write(a)
# f.close()
# name = input("Enter Your Name")
# f = open("names.txt", "r+")
# f.write(name)
# f.close()
# ================== Pointer position-----------------

# f = open("test.txt")
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())

# ----------------------------------------------------------
# ===========With Block File Operation======================
# ----------------------------------------------------------

# with open("test.txt") as f:
#     print(f.readline())
#     print(f.tell())
#     print(f.readline())
#     print(f.tell())

# name = input("Enter Your Name")
# tmp = "nam"
# file_name=tmp+"es.txt"
# f = open(file_name,"r+")
# f.read()
# f.write(name)
# f.write("\n")
# f.close()

def getDate():
    import datetime
    well_format = str(datetime.datetime.now())+"\t"
    # tmp = str(well_format)+"\t"
    return well_format
print(getDate())