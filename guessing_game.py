import random as r
print("Total 3 chances\n")

chances = 3
while chances > 0:
    sys_guess = r.randrange(1, 10)
    user_guess = int(input("Enter a Guess[1-9]: "))
    print(f"\nSystem guess: {sys_guess}\nYour guess: {user_guess}")
    if user_guess == sys_guess:
        print("You Won\n")
        break
    else:
        print("You Loose!\nBetter luck next time\n")
    chances -= 1
