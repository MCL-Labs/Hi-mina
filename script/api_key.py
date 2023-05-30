import random
import string

prefix = "sk-"
suffix_length = 64
suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=suffix_length))

random_string = prefix + suffix

print(random_string)