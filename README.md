# Username_Generator
A Simple Python Script to Generate a Usernames

# Key Features Added:
1. Help Menu:
The display_help() function provides usage instructions and options available for the script.

2. Input Validation:
The script checks if the input file exists and whether each line contains exactly two names (first and last). If a line is invalid, it prints a warning and continues processing.

4. Custom Separator Option:
Users can specify custom separators for username generation using the --separator option.

**For example:** --separator=-,_.

6. Verbose Mode:
The **--verbose** option enables detailed logging of the processing steps, which is useful for debugging.

# Usage Examples:

To see help instructions:

./uname-gen.py --help
To run the script with verbose output and a custom separator:

![1](https://github.com/user-attachments/assets/f922f14d-f050-4fa4-9885-30f1ada44762)
![2](https://github.com/user-attachments/assets/886788de-447c-48f2-9fc6-0b614fe6335f)
![3](https://github.com/user-attachments/assets/d6babc91-d588-4a32-aa5d-526f6ab1f04a)

./uname-gen.py names.txt output.txt --verbose --separator=-,_ 

![5](https://github.com/user-attachments/assets/3e8249f6-c6f9-4763-908c-a673e476355b)

