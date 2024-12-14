#!/usr/bin/env python3 

import sys


def write_uname(first, last):
    separators = ['', '-', '.', '_']
    for sep in separators:
        output_file.write(first + sep + last + '\n')
        output_file.write(first[0] + sep + last + '\n')
        output_file.write(first[0:4]+ sep + last[0:4] + '\n')
        output_file.write(last + sep + first[0] + '\n')
        output_file.write(first + '\n')
        output_file.write(last + '\n')



if len(sys.argv) < 3:
    print("""
    ./uname-gen.py <INPUT FILE> <OUTPUT FILE>

    Input file should contain first and last names separated by spaces with each
    full name it's own line.
    """)
    exit()


output_file = open(sys.argv[2], 'w')
with open(sys.argv[1]) as userfile:
    for line in userfile:
        full_name = line.rstrip().lower().split()
        write_uname(full_name[0], full_name[1])
