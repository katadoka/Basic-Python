# terminal emulator, in which you can move between folders and view files.
# Realize commands: ll, cd, mkdir,touch, and cat.


import os

a = input('>>> ')

if a == 'll':
    print(os.listdir('.'))

elif a == ('cd'):
    path = input('Enter the path >>> ')
    os.chdir(path)
    print(os.listdir('.'))

elif a == 'touch':
    file = input('Enter the name file >>> ')
    action = input('Enter the action file >>> ')
    open(file, action)

elif a == ('mkdir'):
    folder = input('Enter the name folder >>> ')
    os.mkdir(folder)

elif a == 'cat':
    file = input('Enter the name file >>> ')
    read_file = open(file)
    text = read_file.read()
    print(text)
