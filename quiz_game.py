print("Welcome, amici! Take-ah my quiz-ah, per favore!")
playing = input("Do you want to play? si/no ")

if playing.lower() != "si" or "yes":
    print("That's too bad. Game starts now!")
else: 
    print("This was the only option anyway.")
score = 0

answer = input("Como se dice ice icream in italian? ")
if answer.lower() == 'gelato':
    print("ok, good. good. next one won't be this easy.")
    score += 1
else:
    print("gelato!!! nice try though")


answer = input("What is the capital of Italy? ")
if answer.lower() == 'rome':
    print("Ok, world traveller. Relax.")
    score += 1
else:
    print("Oof... good luck on the next one.")


answer = input("Where is the Leaning Tower of Pisa? ")
if answer.lower() == 'pisa':
    print("Well the answer was in the question so I might not count this towards your points.")
    score += 1
else:
    print("Leaning tower of... Pisa...? Pisa... it's Pisa. It was right there.")


answer = input("On the map, Italy is shaped like a...  ")
if answer.lower() == 'boot':
    print("YAY, you know shapes!")
    score += 1
else:
    print("a boot!!")

print("You got " + str(score) + " questions correct!")
print("Which is " + str((score/4) * 100) + "%!")