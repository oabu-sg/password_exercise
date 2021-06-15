Policy = {
   "Upper": 2,
    "Lower": 4,
    "Special": 1,
    "Number": 1
}

def strength_checker():
    print('strength checker')
    pass


output_strength = strength_checker()


def PassGenerate():
    print('password generator')
    pass


def exit_function():
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


def welcome():
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
        user_action = input('Check password strength (1), generate a password (2) or type "exit" to exit.')
        if user_action == '1':
            return strength_checker()
        elif user_action == '2':
            return PassGenerate()

        elif word_exit in user_action.lower():
            return exit_function()
        else:
            print('Invalid input, try again')
            continue


welcome()
