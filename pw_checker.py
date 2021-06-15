import string

def is_Common(Pass):
    with open('Passtext.txt') as File:
        if Pass in File.read():
            return True
        else:
            return False


def users_name_check(first_name, last_name, password):
    if first_name.lower() or last_name.lower() in password.lower():
        return True
    else:
        return False


def DoB_check(Day, Month, Year, password):
    if Year or Month or Day in password:
        return True
    else:
        return False


Chars = list(string.printable)

Policy = {
    "Upper": 2,
    "Lower": 4,
    "Special": 1,
    "Number": 1
}


def strength_checker():

    user_pw = input("Enter password:\n")
    strength_count = 0

    def num():
        num_counter = 0
        for char in user_pw:
            if char in Chars[0:10]:
                num_counter += 1
        if num_counter >= Policy["Number"]:
            return True
        else:
            print("Password does not contain enough numbers")

    def lower_case():
        num_counter = 0
        for char in user_pw:
            if char in Chars[10:36]:
                num_counter += 1
        if num_counter >= Policy["Lower"]:
            return True
        else:
            print("Password does not contain enough lowercase letters")

    def upper_case():
        num_counter = 0
        for char in user_pw:
            if char in Chars[36:62]:
                num_counter += 1
        if num_counter >= Policy["Upper"]:
            return True
        else:
            print("Password does not contain enough uppercase letters")

    def special():
        num_counter = 0
        for char in user_pw:
            if char in Chars[62:95]:
                num_counter += 1
        if num_counter >= Policy["Special"]:
            return True
        else:
            print("Password does not contain enough special characters")
    def pw_length():
        if len(user_pw) >= sum(Policy.values()):
            return True
        else:
            print('Password is too short')


    if num():
        strength_count += 1
    if lower_case():
        strength_count += 1
    if upper_case():
        strength_count += 1
    if special():
        strength_count += 1
    if pw_length():
        strength_count += 1
    if is_Common(user_pw) or users_name_check("Jaydee", "Gbobeh", user_pw) or DoB_check("29", "08", "1997", user_pw):
        strength_count = 0

    if strength_count == 5:
        pw_str = "strong"
    elif strength_count == range(3, 5):
        pw_str = "medium"
    else:
        pw_str = "weak"

    print(f"The strength of your password is: {strength_count}/5, which is {pw_str}")
    return strength_count


strength_checker()
