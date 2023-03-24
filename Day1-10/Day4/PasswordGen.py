import random
import string


def passwordGen():
    password = ""
    for i in range(0, 10):
        password += random.choice(string.ascii_letters + string.digits)
    return password


print(passwordGen())
