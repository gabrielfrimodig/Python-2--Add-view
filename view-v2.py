# -*- coding: utf-8 -*-
"""
@author: gabriel
"""

names   = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]

def view(description, strings):
    n = 1
    
    for x in strings:
        print(f"{n}) {x}")
        n += 1
    return None

view("Lista med namn: ", names)
print()
view("Lista med djur: ", animals)
