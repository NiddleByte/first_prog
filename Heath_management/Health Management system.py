def getDate():
    import datetime
    return datetime.datetime.now()


def add_member():
    name = input("Enter Your Name")
    f = open("names.txt", "r+")
    f.read()
    f.write(name)
    f.write("\n")
    f.close()


def get_member():
    name = int(input("Enter your secret code"))
    while True:
        if name == 1:
            print("Welcome Harry")
            return 1
            break
        elif name == 2:
            print("Welcome Rohan")
            return 2
            break
        elif name == 3:
            print("Welcome Hammed")
            return 3
            break
        else:
            print("Enter Again")
            continue


def get_diet(choice):
    print()
