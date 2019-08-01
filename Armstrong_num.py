n = input("Enter 3 digits number: ")
sum = 0
for i in n:
    m = int(i)**3
    sum += m
if sum == int(n):
    print("{} is an Armstrong number".format(n))
else:
    print("{} is not an Armstrong number".format(n))