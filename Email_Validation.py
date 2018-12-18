import re

# Simple Regex for syntax checking
regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

# Email address to verify
inputAddress = input('Please enter the emailAddress to verify:')
addressToVerify = str(inputAddress)

# Syntax check
match = re.match(regex, addressToVerify)
if match is None:
    print('Bad Syntax, not a Valid Email Address')
else:
    print("Valid Email Address")





