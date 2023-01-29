import os
import shutil
import send2trash as trash

# os delete functions
os.unlink('bacon.txt')  # Will delete a single file off of the hard drive
os.rmdir('PATH')  # will delete only an empty folder from the hard drive

# shutil delete functions
shutil.rmtree('PATH')  # Will delete a folder and all of its contents

# Dry Run
for filename in os.listdir('PATH'):
    if filename.endswith('.txt'):
        # Running this as a comment will not delete any files, just list them out in case of mistakes
        # os.unlink(filename)
        print(filename)

# send to trash module - will send files to the recycle bin instead of instantly deleting them
trash.send2trash('PATH')
