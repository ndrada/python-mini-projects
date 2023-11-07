name = input("Type in your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are at the end of a road and you can only go left or right. Which way do you go? ").lower()

if answer == "left":
    answer = input("You come to a river, You can walk around it or swim accross? Type walk or walk or swim to swim. ")
    if answer == "swim":
        print("You swam across and were eaten by an alligator.RIP")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died of thirst. RIP")
    else: 
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You get to a bridge, it looks wobbly. Do you want to cross it or head back? (cross/go back) ")
    if answer == 'go back':
        print("A hungry lion got you. RIP")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no) ")
        if answer == "yes":
            print("The stranger gave you a bag of gold. You win!!!!")
        elif answer == "no":
            print("The stranger kills you for not talking to them. RIP")
        else:
            print("Not a valid option. You lose.")
    else: 
        print("Not a valid option. You lose.")
else:
    print("Not a valid option.")

print("Thank you for trying! Byeeee")