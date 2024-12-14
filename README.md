# Username_Generator
A Simple Python Script to Generate a Usernames

# Key Features Added:
1. Help Menu:
The display_help() function provides usage instructions and options available for the script.

2. Input Validation:
The script checks if the input file exists and whether each line contains exactly two names (first and last). If a line is invalid, it prints a warning and continues processing.

4. Custom Separator Option:
Users can specify custom separators for username generation using the --separator option. For example: --separator=-,_.

5. Verbose Mode:
The --verbose option enables detailed logging of the processing steps, which is useful for debugging.

# Usage Examples:

To see help instructions:

./uname-gen.py --help
To run the script with verbose output and a custom separator:

./uname-gen.py names.txt output.txt --verbose --separator=-,_ 

This enhanced script provides better usability and flexibility while maintaining clarity in its functionality.
