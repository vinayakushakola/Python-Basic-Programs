n = int(input("Enter number: "))
sum = 0
for i in range(1,n//2 + 1):
    if n % i == 0:
        sum += i
if n == sum:
    print("{} is a perfect number".format(n))
else:
    print("{} is Not perfect no: ".format(n))
