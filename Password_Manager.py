import Password_Generator
from getpass import getpass
from encrypt import encrypt, decrypt
import os
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWRITE


def clearfile():
    with open(filename, 'w') as f:
        f.write("")


def writefile():
    os.chmod(filename, S_IWRITE)


if __name__ == '__main__':
    alreadyfile = input("Do you alreday have an file or not (Yes/No)")
    name = input("Name of your File: ")
    
    filename = r"C:\Users\salve\OneDrive\Desktop\Rohan Work\Python\python Projects\Password_Diary\Files"+f'\{name}.txt'
    if alreadyfile.lower() != 'yes':
        writefile()
        with open(filename, 'w') as f:
            f.write("")

    while True:
        with open(filename, 'r') as f:
            li = f.readlines()

        Operation = int(input(
            "Which Operation you want to do :\n1.Add a New Account.\n2.Delete the Account.\n3.Get Username/Password of an Account.\n4.Change Username or Password Of a Account.\n5.Exit.\n"))

        # Add a new Account in your Password Manager
        if Operation == 1:
            Website = input("Which Website?\n")
            Username = input("Enter The Username")
            if input("Do you Want Generate a password Though Our Password Generator Agorithm?(y/n)").lower() == 'y':
                min_length = int(
                    input("Enter Minimum Length for the password: "))
                numbers = input(
                    "Do you want to  have number (y/n): ").lower() == 'y'
                special_char = input(
                    "Do you want to have special char(y/n): ").lower() == 'y'
                password = Password_Generator.generate_password(
                    min_length, numbers, special_char)
            else:
                password = getpass(
                    "Write the Password(You wont be able see your text.Be Carful): ")

            with open(filename, 'a') as f:
                f.write(f'{encrypt(Website)}'+'\n')
                f.write(f'{encrypt(Username)}'+'\n')
                f.write(f'{encrypt(password)}'+'\n')

    # Remove A Specific Accounnts Username And Password  from the Password Manager
        if Operation == 2:
            remove_website = input(
                "Which Website's Account Do You want to remove?\n")
            clearfile()
            for idx, line in enumerate(li):
                item = line.strip("\n")
                if decrypt(item).lower() == remove_website.lower():
                    li.remove(li[idx + 1])
                    li.remove(li[idx + 1])
                else:
                    with open(filename, 'a') as f:
                        f.write(line)

        # Get Username And Password Of Any Account.
        if Operation == 3:
            search = input("Which Websites Account do you want?\n")
            for idx, line in enumerate(li):
                if decrypt(line.strip("\n")).lower() == search.lower():
                    print(f'{decrypt(li[idx + 1])}')
                    print(f'{decrypt(li[idx + 2])}'+'\n')
                    break

        # Change The Username or Password Of a Account.
        if Operation == 4:
            new_username = None
            new_password = None
            search = input("Which Websites Credentials you want to change: ")
            if input("You want to Change the Password or the Username: ").lower() == 'username':
                new_username = input("Wrute Your New Username :")
            else:
                new_password = getpass(
                    "Enter Your New PAssword(You Wont be able to see your Text. Be Careful): ")

            clearfile()
            with open(filename, 'a') as f:
                for idx, line in enumerate(li):
                    item = line.strip("\n")
                    if decrypt(item).lower() == search.lower():
                        f.write(line)
                        if new_username:
                            li[idx + 1] = encrypt(new_username)+'\n'
                        if new_password:
                            li[idx + 2] = encrypt(new_password)+'\n'
                    else:
                        f.write(line)

        if Operation == 5:
            os.chmod(filename, S_IREAD)
            break


    os.chmod(filename, S_IREAD)
    print("Thank You!")
