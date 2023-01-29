import os

file = open('PATH', 'w')
file.write('Hello World!\nHow are you today?')
file.close()

while True:
    user_input = input('Would you like to delete the file now?')
    if user_input.lower() == 'y':
        break
    else:
        pass

os.remove('PATH')
