#!/usr/bin/env python

# Script to print all hex chars.

def print_all_hex():
    hexlist = []
    for num in range(1,256):
        hexlist.append('\\x%0.2X'.strip() % num)
    allhex = ''.join(hexlist)
    print Chars: 255 skipping  
    print(allhex)
    

print_all_hex()
