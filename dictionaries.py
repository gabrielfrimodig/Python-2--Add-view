# -*- coding: utf-8 -*-
"""
@author: gabriel
"""

users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}
data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}


print("Användare:")
for (x, y) in users.items():
    print(x)
    

print("\nAnvändare och Lösenord:")
for (x, y) in users.items():
    print(f"{x}) {y}")
    

print("\nAnvändare och dess data:")
for (x, y) in users.items():
    print(f"{x}) {data[x]}")
    

g = input("Användare: ")

for (x, y) in data.items():
    if g in data:
        print(f"Data lagrat för {g}: {data[g]}")
        break
    elif g not in data:
        print(f"{g} finns inte med")
        break
