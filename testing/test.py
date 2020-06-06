
def getdate():
    import datetime
    return datetime.datetime.now()

ask_rw = int(input("Enter 1 - read and 2 - write : "))
if ask_rw==2:
    ask_mem = int(input("Enter 1 - harry, 2 - rohan, 3 - hammad : "))
    if ask_mem==1:
        ask_plan = int(input("Enter 1 - Diet, 2 - Exercise : "))
        if ask_plan==1:
            with open("harrydiet.txt", "a") as d:
                d_val = input("What did you eat today? \n")
                d.write("[" + str(getdate()) + "] :" + d_val + "\n")
        elif ask_plan==2:
            with open("harryexercise.txt", "a") as e:
                e_val = input("What workout you did today? \n")
                e.write("[" + str(getdate()) + "] :" + e_val + "\n")

    if ask_mem==2:
        ask_plan = int(input("Enter 1 - Diet, 2 - Exercise : "))
        if ask_plan==1:
            with open("rohandiet.txt", "a") as d:
                d_val = input("What did you eat today? \n")
                d.write("[" + str(getdate()) + "] :" + d_val + "\n")
        elif ask_plan==2:
            with open("rohanexercise.txt", "a") as e:
                e_val = input("What workout you did today? \n")
                e.write("[" + str(getdate()) + "] :" + e_val + "\n")

    if ask_mem==3:
        ask_plan = int(input("Enter 1 - Diet, 2 - Exercise : "))
        if ask_plan==1:
            with open("hammaddiet.txt", "a") as d:
                d_val = input("What did you eat today? \n")
                d.write("[" + str(getdate()) + "] :" + d_val + "\n")
        elif ask_plan==2:
            with open("hammadexercise.txt", "a") as e:
                e_val = input("What workout you did today? \n")
                e.write("[" + str(getdate()) + "] :" + e_val + "\n")

elif ask_rw==1:
    ask_mem = int(input("Enter 1 - harry, 2 - rohan, 3 - hammad : "))
    if ask_mem==1:
        ask_plan = int(input("Enter 1 - Diet, 2 - Exercise : "))
        if ask_plan==1:
            with open("harrydiet.txt") as d:
                print(d.readlines())
        elif ask_plan==2:
            with open("harryexercise.txt") as e:
                print(d.readlines())

    if ask_mem==2:
        ask_plan = int(input("Enter 1 - Diet, 2 - Exercise : "))
        if ask_plan==1:
            with open("rohandiet.txt") as d:
                print(d.readlines())
        elif ask_plan==2:
            with open("rohanexercise.txt") as e:
                print(d.readlines())

    if ask_mem==3:
        ask_plan = int(input("Enter 1 - Diet, 2 - Exercise : "))
        if ask_plan==1:
            with open("hammaddiet.txt") as d:
                print(d.readlines())
        elif ask_plan==2:
            with open("hammadexercise.txt") as e:
                print(d.readlines())

else:
    print("Enter correct value!")