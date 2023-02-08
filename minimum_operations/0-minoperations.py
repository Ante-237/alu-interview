#!/usr/bin/python3

def minOperations(n):

    characters = 1
    operations = 0
    copy = characters

    while characters < n:
        if (n - characters)%2 == 0:
            # perform 
            copy = characters
            characters += copy
            operations += 2
        else:
            if operations == 0:
                operations += 1
            characters += copy
            operations += 1
    return operations
