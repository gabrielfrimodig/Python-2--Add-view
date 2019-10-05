# -*- coding: utf-8 -*-
"""
@author: gabriel
"""


users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}


def login(users):
    username = input("Username: ")
    password = input("Password: ")
    
    while username not in users or password != users[username]:
        print("Invalid username or password")
        username = input("Username: ")
        password = input("Passsword: ")
    else:
        return username
    return None


user = login(users1)
print(f"\nVälkommen {user}")
user = login(users2)
print(f"\nVälkommen {user}")
