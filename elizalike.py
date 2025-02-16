# !/usr/bin/python3
'''
Computational Linguistics Assignment 1: elizalike.py
- Updated by JCrowgey and LPoulson for Spring 2011
- Updated by Olga Zamaraeva for Spring 2018
- Updated by Naomi Tachikawa Shapiro for Spring 2021
- Updated by Sara Ng for Spring 2022
- Updated by Sara Ng for Winter 2025

This script provides a simple automated conversation agent, in the style of
Weizenbaum's Eliza. Invoke by typing:

       python3 elizalike.py

from a command prompt or Unix shell.

This starter script handles input and output, gives an example of a regular
expression in Python, and provides a series of comments (preceded by #) that
outline what has been created for you and what you should add.

I recommend starting by running the script without making any edits.


Regular expressions documentation in python
https://docs.python.org/3/library/re.html
Regular expression Scratch space
https://regexr.com/
'''

# import the re and sys packages
import re
import sys


def reply(text):
    # Python regular expression example ~
    # Replace all instances of "you are" with "---Elizalike-is---":
    # Note how '(\W)' is used to mark word boundaries and '\1' and '\2'
    # are used to retain whatever non-word character was in the input.
    # this allow you to capture the spaces, tabs, and newlines before and
    # after the pattern and add them back to the replaced output.
    pat = r'(\W)?[Yy]ou are(\W)'
    replace = r'\1---Elizalike-is---\2'
    text = re.sub(pattern=pat, repl=replace, string=text)

    # A brief note about the above syntax ~
    # The function `re.sub()` takes three arguments: a regular expression
    # (`pattern`) to search for in the text, a replacement string (`repl`) to
    # replace it with, and the string to operate on (`string`). The function
    # returns a new string, which the above expression is storing in the
    # variable `text`.

    # TODO: Add statements for changing 2nd-person references in the input to
    # 3rd-person --Elizalike-- - style references (temporarily)
    # hint: there are other ways of using "you" besides the phrase you are
    # you will first convert to 3rd person, and then
    # in the block beginning a line 75 you will flip these dummy 3rd person
    # Eliza references to 1st person
    pat = r'(\W)?[Yy]ou were(\W)?'
    replace = r'\1---Elizalike-was---\2'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?[Yy]our(\W)'
    replace = r'\1---Elizalike-s---\2'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?[Yy]ou(\W)?'
    replace = r'\1---Elizalike---\2'
    text = re.sub(pattern=pat, repl=replace, string=text)

    # TODO: Add other transformations of the input that do not have to do with
    # personal deixis:
    # matches instances of 'no one' 'noone' and 'nobody'
    pat = r'(\W)?[Nn]o(( one|one)|body)(\W)?'
    if re.search(pattern=pat, string=text):
        text = "Can you share an example with me?"

    # matches instances of 'friend' and 'friends', but excludes 'boyfriend' and 'girlfriend'
    pat = r'((\W)|^| )[Ff]riends?(\W)?'
    if re.search(pattern=pat, string=text):
        text = "What makes you feel that way?"

    # matches instance of 'lonely' 'stressed' and 'anxious'
    pat = r'(\W)?(lonely|stressed|anxious|sad|depressed)(\W)?'
    match = re.search(pattern=pat, string=text)
    # only runs if a match is found
    if match:
        # creates a variable to store the string from the input that was matched and removes white space
        sub = match.group().strip()
        text = "What do you think has caused you to feel " + sub + "?"

    # macthes instance of 'partner' 'girlfriend' 'boyfriend' 'wife' and 'husband'
    pat = r'(\W)?(partner|((girl|boy)friend)|wife|husband)(\W)?'
    match = re.search(pattern=pat, string=text)
    # only runs if a match is found
    if match:
        # creates a variable to store the string from the input that was matched and removes white space
        sub = match.group().strip()
        text = "Can you tell me more about your " + sub + "?"

    # TODO: Add statements for changing 1st-person references to 2nd-person
    # references:
    pat = r'(\W)?[Ii] am(\W)?'
    replace = r'\1you are\2'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?[Ii] was(\W)?'
    replace = r'\1you were\2'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?[Mm]y(\W)'
    replace = r'\1your\2'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?^[Oo]ur(\W)'
    replace = r'\1Your\2'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)? [Oo]ur(\W)'
    replace = r'\1 your\2'
    text = re.sub(pattern=pat, repl=replace, string=text)
    
    pat = r'(\W)?[Ii](\W)'
    replace = r'\1you\2'
    text = re.sub(pattern=pat, repl=replace, string=text)
    
    pat = r'(\W)?[Ww]e(\W)'
    replace = r'\1you\2'
    text = re.sub(pattern=pat, repl=replace, string=text)

    # TODO: Add statements for changing 3rd-person ---Elizalike--- references to
    # 1st-person references:
    pat = r'---Elizalike-is---'
    replace = r'I am'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'---Elizalike-was---'
    replace = r'I was'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'---Elizalike-s---'
    replace = r'my'
    text = re.sub(pattern=pat, repl=replace, string=text)

    pat = r'(\W)?---Elizalike---(\W)'
    replace = r'I '
    text = re.sub(pattern=pat, repl=replace, string=text)

    # Insert 'Elizalike: ' at the beginning of the text to identify it as
    # Elizalike's response
    text = f'Elizalike: {text}'

    # Return Elizalike's reply to the `main()` function
    return text


def main():
    print("Welcome to Elizalike. Talk to me! (Or type 'bye' to quit.)\n")

    # Start an infinite loop
    while True:

        # Read in the user's input
        text = input("Patient: ")

        # Allow the user to leave therepy
        if re.search(r'^(good)?bye', text, flags=re.I):
            print("Elizalike: Well, it was nice talking to you!\n")
            sys.exit()

        # Get Elizalike's response from the `reply()` function
        rep = reply(text)

        # Print Elizalike's reply to the console
        print(rep)


if __name__ == "__main__":
    main()
