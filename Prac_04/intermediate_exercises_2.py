usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45','BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole','InterpreterInterface', 'StartServer', 'bob']

username = str(input("enter your name"))
if (username in usernames):
    print("access granted!")
else:
    print("access denied!")