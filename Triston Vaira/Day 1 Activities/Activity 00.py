# Use python to produce code below that will:

# Given an email address in email
# Convert the email into a list name `lst'
# The list will contain the individual parts of the email
# Example: email = 'albert@genius.com' -> lst = ['albert', 'genius', 'com']
# NOTE: A variable named email will be available to your code when running.
# NOTE: You must create a variable named lst which contains the required data.
# NOTE: Do not indent your code

##############################################################################
##############################################################################

email = 'albert@genius.com'
lst = email.replace('@', '.').split('.')



