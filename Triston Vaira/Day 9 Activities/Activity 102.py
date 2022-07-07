# Given a username as a string, crack the user's 4 digit pin by repeatedly calling the provided login function. 
# Incorrect attempts to login will raise PermissionError so this, and only this, exception must be caught. 
# Return the pin used to successfully log in.

# login(username,pin)
   
# Returns True if the username and pin are correct. Otherwise raises PermissionError.
# def crack(username):
#     pass


###############################################################################################

def crack(username):
    for potential_pin in range (0,10000):
        pin = str(potential_pin).zfill(4)
        try:
            login(username,pin)
            return pin
        except PermissionError:
            continue