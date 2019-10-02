# -*- coding: utf-8 -*-
"""
@author: gabriel
"""

options = {"a":"Add item", "l":"List items", "q":"Log out"}
software_off = False


# Skriver ut alla alternativ en gång
print("Select an action\n")
for(n, m) in options.items():
    print(f"{n}) {m}")

# Den kör tills ett alternativ är valt
while not software_off:
    valt_alternativ = input("Options: ") #Väntar på input
    for(n, m) in options.items():
        if(valt_alternativ == n):
            print(f"You selected option {n}) {m}")
            software_off = True
