st = input("Enter the string: ")
dic = {}
for i in st:
    if i in dic.keys():
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1

print(dic)
