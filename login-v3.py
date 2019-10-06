# -*- coding: utf-8 -*-
"""
@author: gabriel
"""

users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
options2 = {"r":"Try again", "q":"Quit"}


#=================================
def menu(title, prompt, options):
    print(title)
    
    for (x, y) in options.items(): 
        print(f"{x}) {options[x]}") #Skriver ut alternativen
    
    alternativ = input(prompt)
    while alternativ not in options:
        alternativ = input(prompt) #Fortsätter tills ett giltigt alternativ matas in
    else:
        return alternativ
    return None


#=================================
def login(users):
    username = input("Username: ")
    password = input("Password: ")
    
    while username not in users or password != users[username]: #Om användarnamnet inte hittas, eller om lösenordet inte stämmer överens med användarnamnet.
        dittval = menu("\nInvalid username or password", "Option: ", options2)     
        
        if dittval == "q":
            return None #return = break
        elif dittval == "r":
            return dittval
        
    else: #Om användaren och lösenordet stämmer överens
        return username
    return None


#=================================
user = login(users1)    

if user == None:
    print("User = None")
else:
    while user == "r":
        user = login(users1)
    print(f"\nVälkommen {user}")

