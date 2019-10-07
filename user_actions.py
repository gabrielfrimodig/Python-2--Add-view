# -*- coding: utf-8 -*-
"""
@author: gabriel
"""

user1 = "nisse"
user2 = "bosse"

items1 = ["luva", "vante"]
items2 = ["hammare", "skruv", "spik"]

options1 = {"a":"Add item", "l":"List items", "q":"Log out"}


#===========
def add(prompt, items):
    items.append(input(f"{prompt}"))
    return items

#===========
def view(strings):
    n = 1
    
    for x in strings:
        print(f"{n}) {x}")
        n += 1
    return None

#===========
def menu(title, prompt, options):
    print(title)
    
    for (x, y) in options.items():
        print(f"{x}) {options[x]}")
    
    alternativ = input(prompt)
    while alternativ not in options:
        alternativ = input(prompt)
    else:
        return alternativ
    return None

#============
def user_actions(user, items, options):
    print(f"\n\n\n\n\n\nWelcome {user}")
    view(items)
    
    val = menu("\nSelect an action", "Option: ", options)
    
    while val != "q":
        if val == "a":
            add("\nLägg till: ", items)
            view(items)
            val = menu("\nSelect an action\n", "Option: ", options)
        elif val == "l":
            view(items)
            val = menu("\nSelect an action\n", "Option: ", options)
    
    return items

user_actions(user1, items1, options1)
print(f"Goodbye {user1}, your items: {items1}\n")

user_actions(user2, items2, options1)
print(f"Goodbye {user2}, your items: {items2}\n")







