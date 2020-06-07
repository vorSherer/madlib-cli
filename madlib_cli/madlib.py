from textwrap import dedent

import assets


# Print a welcome message to the user, explaining the Madlib process and command line interactions
def welcome_screen():
    '''
    Welcome message to the user, explaining the Madlib process and command line interactions.
    '''
    opener = ('''
    ***********************************************
    ** Welcome to Madlibs-cli! Provide answers   **
    ** to the prompts given;   For example,      **
    **    a 'noun' is a person, place, or thing; **
    **    a 'plural' means more than one item    **
    **    a 'verb' is an action word;            **
    **    an adjective describes a noun          **
    ** (like 'cold', 'slippery' or 'green') and  **
    **    an 'adverb' typically ends in '-ly.'   **
    ** Press enter after each entry. When all    **
    ** entries have been received, the resulting **
    ** Madlib will be displayed.  Enjoy!         **
    ***********************************************
    ''')

    print(dedent(opener))


# Read a template Madlib file (Example), and parse that file into usable parts.
def read_template():
    '''
    This function opens and reads the contents of the sample template.
    '''
    with open("assets/sample.txt") as sample:
        boilerplate = sample.read()
        return boilerplate



# You need to decide what components of this file are useful, and how to break those useful pieces apart

# Once you know what parts of the template need user input, such as Adjective, prompt the user to submit a series of words to fit each of the required components of the Madlib template.

# With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.

# After the resulting Madlib has been completed, provide the completed response back to the user in the command line.

# Write the completed template (Example)to a new file on your file system (in the repo).




def main():
    welcome_screen()
    read_target()


if __name__ == "__main__":
    main()
