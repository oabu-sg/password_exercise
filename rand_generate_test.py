import string
import random
from random import shuffle
Chars = list(string.printable)
NewPass = []

Policy = {
   "Upper": 3,
    "Lower": 4,
    "Special": 3,
    "Number": 6
}

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

def PassGenerate():

    #Generate_Num = RandomNum()
    policy_length = 0
    while policy_length < Policy['Number']:
        NewPass.append(RandomNum())
        policy_length += 1
    policy_length = 0
    while policy_length < Policy['Lower']:
       NewPass.append(Lower())
       policy_length += 1
    policy_length = 0
    while policy_length < Policy['Upper']:
        NewPass.append(Upper())
        policy_length += 1
    policy_length = 0
    while policy_length < Policy['Special']:
       NewPass.append(Special_Char())
       policy_length += 1
    policy_length = 0
    a = map(str, NewPass)
    JointPass ="".join(a)
    ListPass = list(JointPass)
    shuffle(ListPass)
    FinalString = "".join(ListPass)
    print(NewPass)
    print(FinalString)

PassGenerate()