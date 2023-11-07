import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type rock/paper/scissors to play or q to quit. ').lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        continue

    random_guess = random.randint(0, 2)
    computer_pick = options[random_guess]
    print('Computer picked', computer_pick + '.')

    if (user_input == 'rock' and computer_pick == 'scissors') or (user_input == 'paper' and computer_pick == 'rock') or (user_input == 'scissors' and computer_pick == 'paper') :
        print('You won!')
        user_wins +=1 
    elif user_input == computer_pick:
        print("It's a tie.")
    else:
        print("You lost!!!!!!!!!!!!")
        computer_wins += 1

print("You won", user_wins, "times")
print("The computer won", computer_wins, "times")
print("Buh-bye")
