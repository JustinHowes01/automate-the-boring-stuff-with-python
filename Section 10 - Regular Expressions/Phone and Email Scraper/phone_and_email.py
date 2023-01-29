#! python3

import re, pyperclip

# Create a regex object for phone numbers

phone_regex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
    
(
((\d\d\d)|(\(\d\d\d\)))?   # area code (optional)
(\s|-)                     # first separator
\d\d\d                     # first 3 digits
-                          # separator
\d\d\d\d                   # last 4 digits
(((ext(\.)?\s)|x)           # extension word-part (optional)
(\d{2,5}))?                # extension number-part(optional)
)

''', re.VERBOSE)

# Create a regex for email addresses

email_regex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+        # name part
@                      # @ symbol
[a-zA-Z0-9_.+]+        # domain name
''', re.VERBOSE)

# Get the text off the clipboard

text = pyperclip.paste()

# Extract the email/phone from this list

extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_numbers = []
for phone_number in extracted_phone:
    all_phone_numbers.append(phone_number[0])

# Print the extracted email/phone to a .txt file
results = '\n'.join(all_phone_numbers) + '\n' + '\n'.join(extracted_email)

output_file = open('output.txt', 'w')
output_file.write(results)
output_file.close()
