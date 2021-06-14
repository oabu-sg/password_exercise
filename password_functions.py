# welcome function, collects personal data and what they want to do
import random
import string

# Upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","z"]
# Lower= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w", "x", "y", "z"]
# Number = ["0","1","2","3","4","5","6","7","8","9"]

Chars = list(string.printable)


# print(Chars[0:10]) #number
# print(Chars[10:36]) #Lower
# print(Chars[36:62]) #Upper
# print(Chars[62:95])# Special Chars

def strength_checker():
    user_pw = input("Enter password")
    strength_count = 0
    for char in user_pw:
        if char == Chars[0:10]:
            strength_count += 1
        elif char == Chars[10:36]:
            strength_count += 1
        elif char == Chars[36:62]:
            strength_count += 1
        elif char == Chars[62:95]:
            strength_count += 1

    return strength_count

    print('strength checker')
    pass


output_strength = strength_checker()


def password_generator():
    print('password generator')
    pass


def exit_function():
    print('Exiting...')
    exit()
    pass


def welcome():
    print('Welcome to the Password Hub')

    first_name = str(input('Please enter your first name: '))
    last_name = input('Please enter your last name: ')

    date_of_birth = input('Please enter your date of birth as DD/MM/YYYY: ')  # look this up
    personal_details = [first_name, last_name, date_of_birth]


def menu(first_name):
    word_exit = 'exit'
    running = True
    print(f'Hello {first_name}, enter the corresponding value for what you would like todo:')
    while running:
        user_action = input('Check password strength (1), generate a password (2) or type "exit" to exit.')
        if user_action == '1':
            return strength_checker()
        elif user_action == '2':
            return password_generator()

        elif word_exit in user_action.lower():
            return exit_function()
        else:
            print('Invalid input, try again')
            continue
    pass


# welcome()
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


def user_file(file):
    with open("password.txt", 'a') as file:
        file.write(f"Password strength:{output_strength}\n")


user_file("password.txt")

# Start
# Reading uses password
# Most common checker
# Name, age, DoB
# Password strength checker
# Random generator
# Export Report

# Random number generator that will choice weather it will be upper, lower, special characters, or number
# Second random generator that will decide what will put in that place from the chosen list
