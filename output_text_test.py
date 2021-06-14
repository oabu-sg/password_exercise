# def strength_checker():
#     print('strength checker')
#
# output_strength = stength_checker()
#
# def user_file(file):
#     with open("password.txt", 'a') as file:
#         file.write(f"Password strength:{output_strength}")
#
# user_file("password.txt")
import re
import string
# import re
# #print("".join(a))
Chars = list(string.printable)

def strength_checker():
    user_pw = input("Enter password:\n")
    strength_count = 0
    num = "|".join(Chars[0:10])
    low = "|".join(Chars[10:36])
    upp = "|".join(Chars[36:62])
    spec = "|".join(Chars[62:95])
    match_num = re.search(num)
    match_low = re.search(low)
    match_upp = re.search(upp)
    match_spec = re.search(spec)

    if match_low:
        strength_count +=1
    elif match_upp:
        strength_count +=1
    elif mat
    print(strength_count)
    #for char in user_pw:
    # if char in Chars[0:10]:lower = ",".join(Chars[0:10])
    #     strength_count += 1
    # elif char in Chars[10:36]:
    #     strength_count += 1
    # elif char in Chars[36:62]:
    #     strength_count += 1
    # elif char in Chars[62:95]:
    #     strength_count += 1

    print(strength_count)
pass
strength_checker()

    print('strength checker')
