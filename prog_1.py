""" 1. Write a program to give the following output for the given input

Eg 1: Input: a1b10
       Output: abbbbbbbbbb
Eg: 2: Input: b3c6d15
          Output: bbbccccccddddddddddddddd
The number varies from 1 to 99. """

encrypted=input()
for i in range(len(encrypted)):
    if encrypted[i].isdigit():
        continue
    try:
        print(encrypted[i]*int(encrypted[i+1:i+3]),end='')
    except ValueError:
        print(encrypted[i]*int(encrypted[i+1]),end='')