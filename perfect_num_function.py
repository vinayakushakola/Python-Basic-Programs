n = int(input("From : "))
m = int(input("Where : "))

print("All perfect numbers are: ")
for j in range(n,m+1):
    sum = 0
    for i in range(1,(j//2) + 1):
        if j % i == 0:
            sum += i
    if j == sum:
        print(j)