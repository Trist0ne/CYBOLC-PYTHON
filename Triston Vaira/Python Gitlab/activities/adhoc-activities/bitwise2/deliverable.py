#!/usr/bin/env python

# Translate and return the given linux file permission string as an integer.
# A permission string consists of 3 sets of 3 characters corresponding to permissions for
# owner, group, and others respectively. For each group, 3 characters indicate permissions
# for that group. 

# A first character of 'r' grants read permissions or '-' if read is not permitted.
# A second character of 'w' grants write permissions or '-' if write is not permitted.
# A third character of 'x' grants execute permissions or '-' if execute is not permitted.

# Examples
# 'rwxrwxrwx' grants read, write, and execute for owner, group, and others.
# 'rw-rw----' grands read and write for owner and group only.

# When converting to an integer, each group of 3 characters corresponds to a single decimal
# digit whose binary representation has a 1 for each permission granted and a 0 for each permission denied.

# Examples
# 'rwx' = 111 = 7
# 'rw-' = 110 = 6
# 'r-x' = 101 = 5
# 'r--' = 100 = 4

# The 3 groups, taken together, form the integer.

# Examples
# 'rwxrwxrwx' = 111 111 111 = 511 = 0o777
# 'rw-r-x---' = 110 101 000 = 424 = 0o650

def perms(permissions):
    pass

if __name__ == '__main__':
    a='rwxrwxrwx'
    b='rw-r-x---'

    print(a,oct(q14(a)))
    print(b,oct(q14(b)))
