# welcome function, collects personal data and what they want to do
import random
import string
import time
# Upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","z"]
# Lower= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w", "x", "y", "z"]
# Number = ["0","1","2","3","4","5","6","7","8","9"]

Policy = {
    "Upper": 2,
    "Lower": 4,
    "Special": 1,
    "Number": 1
}

Chars = list(string.printable)
NewPass = []


def welcome():
    global first_name, last_name, personal_details_dict
    print('Welcome to the Password Hub')
    user_name = True
    while user_name:
        try:
            first_name = input('Please enter your first name: ')
            check_numbers_for_str(first_name)
            is_empty(first_name)
            last_name = input('Please enter your last name: ')
            check_numbers_for_str(last_name)
            is_empty(last_name)
            user_name = False
        except TypeError:
            print("Letters only please.")
            continue
        except EOFError:
            print("Please input something....")
            continue
    user_dob = True
    while user_dob:
        try:
            dob_day = input('Please enter the day that you were born as two numbers: ')
            check_numbers_for_int(dob_day, 2)  # it  allows for numbers below the specified amount
            dob_month = input('Please enter the month that you were born as two numbers: ')
            check_numbers_for_int(dob_month, 2)
            dob_year = input('Please enter the year that you were born as four numbers: ')
            check_numbers_for_int(dob_year, 4)
            user_dob = False
        except TypeError:
            print("Numbers only please. Make sure you list the specified amount of numbers")
            continue
        except EOFError:
            print("Please input something....")
            continue
        personal_details_dict = {'First Name': first_name, 'Last Name': last_name, 'DOB Day': dob_day,
                                 'DOB Month': dob_month, 'DOB Year': dob_year}

    return personal_details_dict, menu(first_name)


def menu(first_name):
    word_exit = 'exit'
    running = True
    print(f'\nHello {first_name.capitalize()}, this is the password policy:')
    for key, value in Policy.items():
        print(key, ':', value)
    print("Please enter the corresponding value for what you would like todo:")
    while running:
        user_action = input(
            'Check password strength (1), generate a password (2), enter new personal details (3) or type "exit" to exit.')
        if user_action == '1':
            return strength_checker()
        elif user_action == '2':
            return pass_generate()
        elif user_action == '3':
            return welcome()
        elif word_exit in user_action.lower():
            return exit_function()
        else:
            print('Invalid input, try again')
            continue


# print(Chars[0:10]) #number
# print(Chars[10:36]) #Lower
# print(Chars[36:62]) #Upper
# print(Chars[62:95])# Special Chars

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

    def user_file(file):
        with open("password.txt", 'a') as file:
            for key, value in Policy.items():
                file.write(key + ':' + str(value))
            file.write(f"Each of the policy requirements count as one point.\nIf\nPassword strength:{strength_count} which is {pw_str}")

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
    if is_Common(user_pw) or users_name_check(personal_details_dict['First Name'], personal_details_dict['Last Name'],
                                              user_pw) or DoB_check(personal_details_dict['DOB Day'],
                                                                    personal_details_dict['DOB Month'],
                                                                    personal_details_dict['DOB Year'], user_pw):
        strength_count = 0

    if strength_count == 5:
        pw_str = "strong"
    elif strength_count == range(3, 5):
        pw_str = "medium"
    else:
        pw_str = "weak"

    print(f"The strength of your password is: {strength_count}/5, which is {pw_str}")
    return strength_count, menu(first_name)



def pass_generate():
    policy_length = 0
    NewPass =[]
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
    JointPass = "".join(a)
    ListPass = list(JointPass)
    random.shuffle(ListPass)
    FinalString = "".join(ListPass)
    print(NewPass)
    print(FinalString)
    time.sleep(10)
    menu(first_name)


def exit_function():
    strength_checker.user_file()
    print('Exiting...')
    exit()
    pass


def check_numbers_for_str(is_num):
    user_prompt = True
    while user_prompt:
        if is_num.isdigit():
            raise TypeError
        else:
            return welcome


def check_numbers_for_int(is_num, num_of_dob):
    user_prompt = True
    if len(is_num) != num_of_dob:
        raise TypeError
    else:
        while user_prompt:
            if is_num.isdigit():
                return welcome
            else:
                raise TypeError


def is_empty(name):
    if name == '':
        raise EOFError
    else:
        return welcome


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


# Start
# Reading uses password
# Most common checker
# Name, age, DoB
# Password strength checker
# Random generator
# Export Report

# Random number generator that will choice weather it will be upper, lower, special characters, or number
# Second random generator that will decide what will put in that place from the chosen list
welcome()
