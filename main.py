# -*- coding: utf-8 -*-
"""
@author: gabriel
"""

option_inloggad = {"a":"Add item", "l":"List items", "q":"Log out"}
option_retry = {"r":"Try again", "q":"Quit"}

def main():
    users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
    data  = {"nisse":["luva", "vante"],  "stina":[], "bosse":["gräs", "mjölk"]}
    options_start = {"l":"Log in", "q":"Quit"}
    
    operation = True
    
    while operation:
        start = menu("\n\n\n\nWelcome to Lagra (TM)\n------------------", "Option: ", options_start)
        if start == "l": #Om man vill logga in
            user = login(users)
            
            if user == "r":
                user = login(users)
            elif user != None: 
                data = user_actions(user, data, option_inloggad) #den ändras bara om något lagts till
        else:
            operation = False

#===========
def add(prompt, user, data):
    data[user].append(input(f"{prompt}"))
    return data

#===========
def view(user, data):
    n = 1
    
    for x in data[user]:
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

#============
def user_actions(user, data, options):
    print(f"\n\n\nWelcome {user}\n--------------")
    view(user, data) #Visar all data
    val = menu("\nSelect an action", "Option: ", options)
    
    while val != "q":
        if val == "a":
            add("\nLägg till: ", user, data)
        elif val == "l":
            print("här är din data")
        view(user, data)
        val = menu("\nSelect an action\n", "Option: ", options)
    
    return data

#============
def login(users):
    username = input("Username: ")
    password = input("Password: ")
    
    while username not in users or password != users[username]: #Om inloggningen misslyckas
        try_again = menu("\n\nInvalid username or password\n----------------------------", "Option: ", option_retry) #Skickar valmöjligheten 2        
        
        if try_again == "r":
            return try_again
        elif try_again == "q":
            return None
        #return try_again
    else: #Om användaren och lösenordet stämmer överens
        return username




main()




