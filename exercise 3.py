n = int(input("Enter No of rows"))
b = int(input("Enter 1 or 0"))

if b == 0:
    temp = n
    while temp > 0:
        print(temp * "*")
        temp = temp - 1
else:
    temp = 0
    while temp < n:
        temp = temp + 1
        print(temp * "*")
