# -*- coding: utf-8 -*-
"""
@author: gabriel
"""

strings = []

def add(strings):
    strings.append(input("Lägg till en anka: "))
    return strings


def view(description, strings):
    n = 1
    
    print(f"Du har matat in följande {description} sträng(ar)")
    
    for x in strings:
        print(f"{n}) {x}")
        n += 1
    return None


numbers = int(input("Hur mågna strängar vill du lägga till = "))

for x in range (0, numbers):
    add(strings)

view(numbers, strings)
