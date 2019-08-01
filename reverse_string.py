def reverse(name):
    r = ""
    length = len(name) - 1
    while length >= 0:
        r = r + name[length]
        length -= 1
    return r

output = reverse("Vinayak Ushakola")

print(output)
