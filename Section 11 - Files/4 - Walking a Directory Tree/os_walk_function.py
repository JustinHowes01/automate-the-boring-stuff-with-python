import os

for folder_name, subfolders, filenames in os.walk('PATH'):
    if not subfolders:
        subfolders = 'None'
    if not filenames:
        filenames = 'None'

    print()
    print('The folder is ' + folder_name)
    print('The subfolders in ' + folder_name + ' are: ' + str(subfolders))
    print('The filenames in ' + folder_name + ' are: ' + str(filenames))
    print()

    # Things you can do with walking
    '''
    for subfolder in subfolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)

    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(folder_name, file), os.join(folder_name, file + '.backup'))
    '''
