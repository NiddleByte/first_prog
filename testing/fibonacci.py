def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

    # Write your code here.

# n = int(input())
# print(fibonacci(n))



def fibonacci_seq(n):
    a = 0 #first value
    b = 1 #second value
    if n==0:
        print("0")
    elif n == 1:
        print("1")
    else:
        # print(a,b, end=" ")
        for i in range(n-2):
            c = a + b   #1 ,
            a = b       #1
            b = c       #1
            print(b , end=" ")
fibonacci_seq(20)