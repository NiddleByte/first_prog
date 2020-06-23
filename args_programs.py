def args_fun(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum
print(args_fun(1,2,3,4,5))



def args_fun(num,*args):
    sum = 0
    print(num)
    print(args)
    for i in args:
        sum +=i
    return sum
print(args_fun(1,2,3,4,5))


# ========= args as arguments=========

