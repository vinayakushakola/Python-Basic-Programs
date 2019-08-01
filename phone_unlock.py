set_password = input("Set password: ")
chances = 3
while chances > 0:
    chances -= 1
    get_password = input("Enter the password: ")
    if get_password == set_password:
        print("phone unlocked")
        break
    else:
        print("Invlid password\n")

if get_password == set_password:
    print("welcome to Screen")
else:
    print("Try Again! after 30 seconds")
