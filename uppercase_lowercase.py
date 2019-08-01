# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def str(n):
    count_cap = 0
    count = 0
    for i in n:
        oi = ord(i)
        if oi >= 65 and oi <= 91:
            count_cap += 1

        else:
            count += 1

    print(f"Upper case {count_cap}")
    print(f"Lower case {count}")
    return count_cap
    return count


str("PyThOn")
