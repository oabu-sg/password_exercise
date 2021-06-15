import random

sample_str = "PYnative"  #jointpass
# Original string
print(sample_str)
# 'PYnative'

# convert string into list
char_list = list(sample_str)
# shuffle list
random.shuffle(char_list)

# convert list to string
final_str = ''.join(char_list)

# shuffled list
print(final_str)
# Output 'tiaeYPvn'