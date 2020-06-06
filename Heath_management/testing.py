def getDate():
    import datetime
    well_format = str(datetime.datetime.now()) + "\t \t"
    return well_format


def diet_plan(customer_name):
    print("Here is your daily diet")
    filename = customer_name + "_diet.txt"
    fp = open(filename, "r+")
    print(fp.read())
    tmp = input("Add your todays diet \t")
    todays_data = tmp + "\t" + getDate()
    fp.write("\n")
    fp.write(todays_data)
    fp.write("\n")
    fp.close()


def exercise(customer_name):
    print("Here is Your yesterday's workout")
    filename = customer_name + "_workout.txt"
    fp = open(filename, "r+")
    print(fp.read())
    tmp = input("Add your todays workout\t")
    todays_data = tmp + "\t" + getDate()
    fp.write("\n")
    fp.write(todays_data)
    fp.write("\n")
    fp.close()


def forName(name):
    customer_name = name
    print("Welcome\t", customer_name)
    choice = int(input("Enter 1 for diet and 2 for exercise"))
    if choice == 1:
        diet_plan(customer_name)
    elif choice == 2:
        exercise(customer_name)
    else:
        print("Please Enter valid number")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ----------------------------- Our Program ------------------------
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=++

print("Welcome to Super Diet and exercise planner\n")
print("1 = Harry \n2 = Rohan \n3 = Hammad")
name = int(input("Enter 1 / 2 / 3\t"))
if name == 1:
    forName("harry")
elif name == 2:
    forName("rohan")
elif name == 3:
    forName("hammad")
else:
    print("Please enter valid keywords")
