def removeDuplicate(str):
    s = set(str)
    s = "".join(s)
    t = ""
    for i in str:
        if i in t:
            pass
        else:
            t += i

    return t


def convert(a, val):
    if a == 0:
        return int("".join(sorted(str(val))))
    else:
        return int("".join(sorted(str(val))[::-1]))


count = 0
for iterator in range(1000, 10000):
    string = removeDuplicate(str(iterator))
    number = int(string)
    if len(string) == 4:
        i = 0
        while number != 6174:
            number = convert(1, number) - convert(0, number)
            i += 1
        else:            
            print(F"The number is {number}. Found in {i} times.")
            count += 1

print("Numbers here: " + count)

input()
