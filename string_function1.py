import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and MacOS
    else:
        os.system('clear')

def capitalize_string(input_str):
    return input_str.capitalize()

def is_lower_case(input_str):
    return str(input_str.islower())

def convert_to_lower_case(input_str):
    return input_str.lower()

def convert_to_upper_case(input_str):
    return input_str.upper()

def split_sentence(input_str):
    return input_str.split()

def count_vowels(input_str):
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_str if char in vowels)

def reverse_string(input_str):
    return input_str[::-1]

def find_substring(input_str, substring):
    return input_str.find(substring)

def replace_substring(input_str, old_substring, new_substring):
    return input_str.replace(old_substring, new_substring)

def is_alpha_numeric(input_str):
    return str(input_str.isalnum())
def func():
 print("Major String function")
 print("1. Capitalize")
 print("2. Check whether the given string is lowercase or not")
 print("3. Change all the characters into lowercase for the given string")
 print("4. Change all the characters into uppercase for the given string")
 print("5. Split the sentence into words")
 print("6. Count Vowels")
 print("7. Reverse String")
 print("8. Find Substring")
 print("9. Replace Substring")
 print("10. Check if the string is alphanumeric")
 print("11. Exit")
func()
n = int(input("Enter your choice: "))
string = input("Enter the string: ")

while n != 11:
    if n == 1:
        print("Answer:", capitalize_string(string))
    elif n == 2:
        print("Answer:", is_lower_case(string))
    elif n == 3:
        print("Answer:", convert_to_lower_case(string))
    elif n == 4:
        print("Answer:", convert_to_upper_case(string))
    elif n == 5:
        print("Answer:", split_sentence(string))
    elif n == 6:
        print("Answer:", count_vowels(string))
    elif n == 7:
        print("Answer:", reverse_string(string))
    elif n == 8:
        substring = input("Enter the substring to find: ")
        print("Answer:", find_substring(string, substring))
    elif n == 9:
        old_substring = input("Enter the old substring: ")
        new_substring = input("Enter the new substring: ")
        print("Answer:", replace_substring(string, old_substring, new_substring))
    elif n == 10:
        print("Answer:", is_alpha_numeric(string))
    else:
        print("Invalid Number")

    query = input("Do you want to continue further? (Yes/No)")
    clear_screen()
    if query.lower() in ["yes", "y"]:
        func()
        n = int(input("Enter your choice: "))
        string = input("Enter the string: ")
    else:
        n = 11
