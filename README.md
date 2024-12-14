# AD Username_Generator
AD Username Creator: Generate Unique Usernames for Active Directory can be particularly useful for penetration testers and red teamers in several ways:

## Username Enumeration:
The script can generate potential usernames based on common naming conventions used in organizations. This is crucial during the reconnaissance phase of a penetration test, where identifying valid usernames can lead to further exploitation attempts, such as password spraying or credential stuffing attacks.

## Testing Naming Conventions:
By generating usernames that conform to typical formats (e.g., first initial + last name), pentesters can validate the effectiveness of their username enumeration strategies. This helps in understanding how user accounts are structured within the target organization, which can inform subsequent attack vectors.

## Integration with Other Tools:
The generated usernames can be fed into other tools used for Active Directory attacks, such as Kerbrute or Hashcat, which are designed for enumerating users or cracking passwords. This integration enhances the efficiency of the testing process.

## Social Engineering Preparation:
Knowing the likely usernames allows red teamers to craft more convincing phishing attacks. They can tailor their messages based on the generated usernames, making it easier to trick users into revealing credentials.

## Automating User List Creation:
The tool automates the tedious task of creating a list of potential usernames, allowing pentesters to focus on more strategic aspects of their assessments rather than manual enumeration.

# Key Features Added:
1. Help Menu:
The display_help() function provides usage instructions and options available for the script.

2. Input Validation:
The script checks if the input file exists and whether each line contains exactly two names (first and last). If a line is invalid, it prints a warning and continues processing.

4. Custom Separator Option:
Users can specify custom separators for username generation using the --separator option.
For example: --separator=-,_.

6. Verbose Mode:
The **--verbose** option enables detailed logging of the processing steps, which is useful for debugging.

# Installation Process:
```bash
git clone https://github.com/s4m98/Username_Generator.git

sudo chmod +x uname_gen.py

python3 uname_gen.py -h
```

# Usage Examples:

To see help instructions:

**./uname-gen.py --help**
To run the script with verbose output and a custom separator:

![1](https://github.com/user-attachments/assets/f922f14d-f050-4fa4-9885-30f1ada44762)
![2](https://github.com/user-attachments/assets/886788de-447c-48f2-9fc6-0b614fe6335f)
![3](https://github.com/user-attachments/assets/d6babc91-d588-4a32-aa5d-526f6ab1f04a)

## ./uname-gen.py names.txt output.txt --verbose --separator=-,_ 

![5](https://github.com/user-attachments/assets/3e8249f6-c6f9-4763-908c-a673e476355b)

