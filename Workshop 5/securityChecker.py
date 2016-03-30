"""Ask the user for a potential name and check that it does not already exist.
Append if so."""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
            'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
            'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

potential_username = input("Enter a username: ")
isValid = False
while not isValid:
    if potential_username not in usernames:
        print("Access denied")
        potential_username = input("Enter a username: ")
    else:
        print("Access granted!")
        isValid = True