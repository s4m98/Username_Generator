#!/usr/bin/env python3 

import sys
import os

def display_help():
    help_text = """
    Usage: ./uname-gen.py <INPUT FILE> <OUTPUT FILE> [OPTIONS]

    Input file should contain first and last names separated by spaces, with each
    full name on its own line.

    Options:
      --help, -h          Show this help message and exit.
      --verbose, -v       Enable verbose output for detailed logging.
      --separator <sep>   Specify a custom separator for username generation (default: '-', '.', '_').

    Example:
      ./uname-gen.py names.txt output.txt --verbose
    """
    print(help_text)

def write_uname(first, last, separators):
    for sep in separators:
        output_file.write(first + sep + last + '\n')
        output_file.write(first[0] + sep + last + '\n')
        output_file.write(first[0:4] + sep + last[0:4] + '\n')
        output_file.write(last + sep + first[0] + '\n')
        output_file.write(first + '\n')
        output_file.write(last + '\n')

# Check command line arguments
if len(sys.argv) < 3:
    display_help()
    exit()

# Initialize variables
input_file = sys.argv[1]
output_file_path = sys.argv[2]
verbose = False
custom_separator = ['-', '.', '_']  # Default separators

# Process command line options
for arg in sys.argv[3:]:
    if arg in ['--help', '-h']:
        display_help()
        exit()
    elif arg in ['--verbose', '-v']:
        verbose = True
    elif arg.startswith('--separator='):
        custom_separator = arg.split('=')[1].split(',')
    else:
        print(f"[!] Unknown option: {arg}")
        display_help()
        exit()

# Check if input file exists
if not os.path.isfile(input_file):
    print(f"[!] Input file '{input_file}' does not exist!")
    exit()

# Open the output file for writing
with open(output_file_path, 'w') as output_file:
    with open(input_file) as userfile:
        for line in userfile:
            full_name = line.rstrip().lower().split()
            if len(full_name) != 2:
                print(f"[!] Invalid line in input file: '{line.strip()}'")
                continue  # Skip invalid lines
            
            first_name, last_name = full_name
            
            if verbose:
                print(f"[DEBUG] Generating usernames for: {first_name} {last_name}")
            
            write_uname(first_name, last_name, custom_separator)

if verbose:
    print("[DEBUG] Username generation completed.")
