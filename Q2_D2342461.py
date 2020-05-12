# Q2.py
# TMA03 19J Question 2

"""
This flashcard program allows the user to choose entry from an easy or hard glossary.
In response, the program randomly picks an entry from the chosen glossary
entries. It shows the entry. After the user presses return, the
program shows the definition of that particular entry.
The user can repeatedly ask for an entry from both glossaries and also
has the option to quit the program instead of seeing
another entry.
"""

from random import *

# Set up 'easy' and 'hard' glossaries

easy_glossary = {'word1':'definition1',
                 'word2':'definition2',
                 'word3':'definition3'}

hard_glossary = {'word4':'definition4',
                 'word5':'definition5',
                 'word6':'definition6'}

# Modify this function for part aii.

def show_flashcard():
    """ Show the user a random key from
        easy_glossary if user_input == 'e' and from the
        hard_glossary if user_input == 'h', then ask them
        to define it.
        Show the definition when the user presses return.    
    """
    if user_input == 'e':
        random_key = choice(list(easy_glossary))
        print('Define: ', random_key)
        input('Press return to see the definition')
        print(easy_glossary[random_key])

    elif user_input == 'h':
        random_key = choice(list(hard_glossary))
        print('Define: ', random_key)
        input('Press return to see the definition')
        print(hard_glossary[random_key])


# The interactive loop. Modify this for part aiv.

exit = False
while not exit:
    user_input = input('Enter e for a flashcard from the easy list, h for the hard list and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 'e'or user_input == 'h':
        show_flashcard()
    else:
        print('You need to enter either e, h or q.')
