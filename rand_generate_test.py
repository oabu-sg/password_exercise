import string
import random

Chars = list(string.printable)
NewPass = []


def RandomNum():
    randomNum = random.randint(1, 4)
    return randomNum


def RandomPass():
    randomNum = random.randint(0, 10)
    return Chars[randomNum]


def Lower():
    randomNum = random.randint(10, 36)
    return Chars[randomNum]


def Upper():
    randomNum = random.randint(36, 62)
    return Chars[randomNum]


def Special_Char():
    randomNum = random.randint(62, 95)
    return Chars[randomNum]

i = 0
while i < 5:
    Generate_Num = RandomNum()
    if Generate_Num == 1:
        NewPass.append(RandomNum())
    elif Generate_Num == 2:
        NewPass.append(Lower())
    elif Generate_Num == 3:
        NewPass.append(Upper())
    elif Generate_Num == 4:
        NewPass.append(Special_Char())

a = map(str, NewPass)
print("".join(a))
