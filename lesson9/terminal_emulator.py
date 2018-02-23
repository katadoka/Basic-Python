# terminal emulator, in which you can move between folders and view files.
# Realize commands: ll, cd, mkdir,touch, and cat.


import os


def terminal_emulator(i):
    if i[0] == 'll':
        print(os.listdir('.'))

    elif i[0] == 'cd':
        os.chdir(i[1])

    elif i[0] == 'touch':
        with open(i[1], 'w') as h:
            pass

    elif i[0] == 'mkdir':
        os.mkdir(i[1])

    elif i[0] == 'cat':
        with open(i[1], 'r') as g:
            print(g.read())

    elif i[0] == 'exit':
        exit()

    return terminal_emulator(input('>>> ').split())

i = input('>>> ').split()

terminal_emulator(i)
