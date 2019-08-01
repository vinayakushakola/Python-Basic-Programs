import math as m

num = input("Enter a number: ")

sum = 0
for i in str(num):
    c = m.factorial(int(i))
    sum += c
if sum == int(num):
    print(f"Strong number: {num}")
else:
    print(f"Not a strong number: {num}")
