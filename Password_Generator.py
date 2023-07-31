import string
import random

def generate_password(min_length,numbers=False,special_char=False):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters=letters
    if numbers:
        characters+=digits
    if special_char:
        characters+=special

    meets_criteria=False
    has_numbers=False
    has_special=False

    pwd=''
    while not meets_criteria or len(pwd)<min_length:
        new_char=random.choice(characters)
        pwd+=new_char

        if new_char in digits:
            has_numbers=True
        if new_char in special:
            has_special=True
        meets_criteria=True
        if numbers:
            meets_criteria=has_numbers
        if special_char:
            meets_criteria=meets_criteria and has_special

    return pwd


if __name__=='__main__':
    min_length=int(input("Enter Minimum Length fpr the password: "))
    numbers=input("Do you want to  have number (y/n): ").lower()=='y'
    special_char=input("Do you want to have special char(y/n): ").lower()=='y'
    # print(generate_password(min_length,numbers,special_char))