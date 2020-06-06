no_rows = int(input("Enter No of rows"))
tmp = int(input("Enter 1 or 0"))
bool = bool(tmp)
# if b == 0:
#     temp = n
#     while temp > 0:
#         print(temp * "*")
#         temp = temp - 1
# else:
#     temp = 0
#     while temp < n:
#         temp = temp + 1
#         print(temp * "*")
#
#


if bool == True:
    for i in range ( 1 , no_rows+1):
        for j in range (1 ,i+1):
            print("*",end=" ")
        print()
elif bool == False:
    for i in range(no_rows,0,-1):
        for j in range (1,i+1):
            print("*",end=" ")
        print()
