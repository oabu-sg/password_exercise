import string

Chars = list(string.printable)

Policy = {
   " Upper": 2,
    "Lower": 4,
    "Special": 1,
    "Number": 1
}

def strength_checker():
    user_pw = input("Enter password:\n")
    strength_count = 0
    def num():
        for char in user_pw:
            if char in Chars[0:10] == Policy["Number"]:
                return True

    def lower_case():
        for char in user_pw:
            if char in Chars[10:36] == Policy["Lower"]:
                return True

    def upper_case():
        for char in user_pw:
            if char in Chars[36:62] == Policy["Upper"]:
                return True

    def special():
        for char in user_pw:
            if char in Chars[62:95] == Policy["Special"]:
                return True

    def pw_length7():
        if len(user_pw) >= 7:
            return True

    def pw_length15():
        if len(user_pw) >= 15:
            return True

    if num():
        strength_count += 1
    if lower_case():
        strength_count += 1
    if upper_case():
        strength_count += 1
    if special():
        strength_count += 1
    if pw_length7():
        strength_count += 1
    if pw_length15():
        strength_count += 1

    print(strength_count)


strength_checker()