# def stength_checker():
#     print('strength checker')
#
# output_strength = stength_checker()
#
# def user_file(file):
#     with open("password.txt", 'a') as file:
#         file.write(f"Password strength:{output_strength}")
#
# user_file("password.txt")

def strength_checker():
    user_pw = input("Enter password")
    strength_count = 0
    for char in user_pw:
        if char in Chars[0:10]:
            strength_count += 1
        elif char == Chars[10:36]:
            strength_count += 1
        elif
    return strength_count