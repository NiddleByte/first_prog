guess = 18
total_chance = 10
while True:

    if total_chance <= 0:
        print("You do not have more chance !!\n==============\n|| Game Over ||\n===============")
        break
    print("==========================")
    print("Your Total Chance left =[", total_chance, end=" ]")
    print("\n==========================\n")

    val = input("Enter your guess \t")
    if val.isnumeric():
        val = int(val)
        total_chance = total_chance - 1
        if val > guess:
            print("Greater value is Given\n")
            continue
        elif val < guess:
            print("Lower Value is Given\n")
            continue
        else:
            print("You Won !!!! \nYour prediction is correct ")
            print("Your left chances are =", total_chance)
            break
    else:
        print("Please enter valid values only !")
        continue