Password Generator 1.0
# Author : Nhlanhla Richard Nqoko
# Github : https://github.com/richardnqoko
# Date   : 21/12/2022

import random
import string

tmp = num = ""
lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
special = "!@#$&*_"
numeric = [int(n) for n in range(10)]

for number in numeric:
    num+=str(number)

numeric = num

passkey = lowerCase + upperCase + numeric + special
length = 8

password = tmp.join(random.sample(passkey, length))

print("New Password is: " + password)
