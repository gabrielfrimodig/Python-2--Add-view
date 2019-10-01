# -*- coding: utf-8 -*-
"""
@author: gabriel
"""

ducks = ["knatte", "fnatte", "tjatte"]

def utskrift (ankor):
    print("Lista med ankor:",ducks)
    return None

utskrift(ducks)
ducks.append(input("Lägg till en anka: "))
utskrift(ducks)
    






