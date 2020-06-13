from textwrap import dedent

import assets


# Print a welcome message to the user, explaining the Madlib process and command line interactions
def welcome_screen():
    '''
    Welcome message to the user, explaining the Madlib process and command line interactions.
    '''
    opener = ('''
    **  **  **  **  **  **  **  **  **  **  **  **  **  **  **  **  
    Welcome to Madlibs-cli! Provide answers to the prompts given;   
    For example, 
    * a 'noun' is a person, place, or thing; 
    * a 'plural' means more than one item; 
    * a 'verb' is an action word; 
    * an adjective describes a noun (like 'cold', 'slippery' or 'green') and 
    * an 'adverb' typically ends in '-ly.' 
    Press enter after each entry. When all entries have been received, the result will be displayed.  Enjoy! 
    **  **  **  **  **  **  **  **  **  **  **  **  **  **  **  **  
    ''')

    print(dedent(opener))


# Read a template Madlib file (Example), and parse that file into usable parts.
def read_template(source):
    '''
    This function opens and reads the contents of the template and returns a "stripped" version.
    '''
    try:
        with open(source, 'r') as template:
            stripped_content = template.read().strip()
            # print("stripped: ", stripped_content)
            return stripped_content
    except:
        return "Error reading source file into read_template function."

# Create and test a parse function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.
def parse_source(source):
    '''
    This function takes in a string template and returns a separate list of selected language parts.
    '''
    try:
        content = read_template(source)
        word_list = []
        word_end = 0
        fill_in_count = content.count('{')
        for idx in range(fill_in_count):
            word_start = content.find('{', word_end) +1
            word_end = content.find('}', word_start)
            parsed_word = content[word_start:word_end]
            word_list.append(parsed_word)
        return word_list
    except:
        return "Error while attempting to use parse_source function."

# def empty_template(source):
#     '''
#         This function takes in a string template and returns a string with language parts removed.
#     '''
#     try:
#         content = read_template(source)
#         word_end = 0
#         fill_in_count = content.count('{')
#         for idx in range(fill_in_count):
#             word_start = content.find('{', word_end) +1
#             word_end = content.find('}', word_start)
#             template = content.replace([word_start:word_end], "")
#             word_list.append(parsed_word)
#         return template
#     except:
#         return "Error while attempting to use empty_template function."

# Once you know what parts of the template need user input, such as Adjective, prompt the user to submit a series of words to fit each of the required components of the Madlib template.
def prompt_user_input():
    '''
    This function uses the word_list from parse_source function to request corresponding input from the user.
    '''
    try:
        pass
    except:
        return "Error while attempting to use prompt_user_input function."

# With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.


# Merge "Dictionary" values with corresponding positions in "vacated" template, remove the curly braces.
def merge():
    '''
    This function takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
    '''
    try:
        pass
    except:
        return "Error while attempting to use merge function."
# After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
# Display the file contents on the command line.
def display_results():
    '''
    This function displays the resulting text from the merge function on the command line.
    '''
    try:
        pass
    except:
        return "Error while attempting to use display_results function."

# Write the completed template (Example)to a new file on your file system (in the repo).
def save_results_to_file():
    '''
    This function saves the resulting text from the merge function to a local text file.
    '''
    try:
        pass
    except:
        return "Error while attempting to save results to file."



def main():
    welcome_screen()
    read_template("assets/target.txt")


if __name__ == "__main__":
    main()
