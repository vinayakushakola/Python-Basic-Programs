seq = 10

a = 0
b = 1
print(b)
for i in range(seq):
    c = a+b
    a = b
    b = c
    print(c)