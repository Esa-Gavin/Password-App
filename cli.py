#! /usr/bin/env python3.9
import random
import string
from classes import User, Credentials

def create_account(username, password):
    ''' function to create a new user '''

    new_user = User(username, password)
    return new_user


def create_credentials(account, username, password):
    ''' function to create new credentials '''

    new_credentials = Credentials(account, username, password)
    return new_credentials


def kuokoa_user(mtumiaji):
    ''' function to save user '''

    mtumiaji.save_user()


def kuokoa_credentials(hati):
    ''' function to save credentials '''

    hati.save_credentials()


def display_mtumiaji():
    ''' function that displays watumiaji/users '''

    return User.display_users()


def display_hati():
    ''' function that displays credentials '''

    return Credentials.display_credentials()


def log_in(user, password):
    ''' function to log in users '''

    verified_mtumiaji = User.verified_users(user, password)
    return verified_mtumiaji

def find_credential(account):
    ''' function to find credentials '''

    return Credentials.find_by_account(account)


def generatePassword(stringLength=8):
    """Generate a random password string of letters and digits and special characters"""
    password = string.ascii_uppercase + \
        string.ascii_lowercase + string.digits + "~!@#$%^&*"
    return ''.join(random.choice(password) for i in range(stringLength))

def password_app():
    print(" ")
    print(" ")
    print("Hello there Choomba, what is your name?")
    print(" ")
    print(" ")
    print(" ")
    username = input()

    print(f"Hello {username}. What would you like to do?")
    print('\n')
    while True:
        print("-"*130)
        print(""" Use these short codes
        1. cc - CREATE A NEW CREDENTIAL
        2. dc - DISPLAY ACCOUNTS
        3. lg - LOGIN TO ACCOUNT
        4. fc - FIND A CREDENTIAL
        5. d - DELETE A CREDENTIAL
        6. gp - GENERATE A PASSWORD
        7. ex - EXIT THE APPLICATION""")

        print(" ")
        print("     TYPE IN A SHORT CODE PLEASE")
        print(" ")

        short_code = input().lower()
        if short_code == 'cc':
            print(" ")
            print("-" * 130)
            print("     ***CREATE A NEW CREDENTIAL***")
            print(" ")
            print("what is your username that you'd like to use?")
            print(" ")
            jina = input().lower()
            print("what is the name of the account")
            print(" ")
            user_name = input().lower()
            print("what is the password to your account?")
            print(" ")
            pass_word = input().lower()
            kuokoa_user(create_account(jina, user_name))
            print('\n')
            kuokoa_credentials(create_credentials(
                user_name, pass_word, pass_word))
            print('\n')
            print("-" * 100)
            print(
                f"Your new account { jina } { user_name } has been successfully been created")
            print('\n')
        elif short_code == 'dc':
            if display_mtumiaji():
                print(" ")
                print("User name")
                print(" ")
                print('\n')
                for user in display_mtumiaji():
                    print(f"{ jina }")
                for credentials in display_hati():
                    print(f"{ pass_word }")
                    print(" ")
            else:
                print('\n')
                print("-" * 130)
                print(" ")
                print("               *** PLESE DO CREATE AN ACCOUNT ***")
                print("                 *** You have not created an account yet ***")
                print(" ")
        elif short_code == 'gp':
            password = generatePassword()
            return password

        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.username} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("The Credential does not exist")
                print('\n')

        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")


        elif short_code == 'lg':
            print('\n')
            print("*" * 30)
            print("Log in to your account")
            print("*" * 30)

            print("Enter your username")
            userName = input().lower()

            print("Enter your password")
            userPassword = input().lower()

            if log_in(userName, userPassword):
                print('\n')
                print("-"*130)
                print(f"Welcome { userName } to your credentials")
                print("-"*130)

                while True:
                    print('''Please choose a short code \n
                        cc - CREATE A NEW CREDENTIAL
                        dc - DISPLAY ACCOUNTS
                        lg - LOGIN TO ACCOUNT
                        fc - FIND A CREDENTIAL
                        d - DELETE A CREDENTIAL
                        gp - GENERATE A PASSWORD
                        ex - EXIT THE APPLICATION''')
                    short_code = input().lower()

                    if short_code == "cc":
                        print('\n')
                        print("New Credential")
                        print("-"*15)

                        print("Type your name...")
                        credential_name = input().lower()

                        print("Type your password")
                        credential_password = input().lower()

                        kuokoa_credentials(create_credentials(
                            credential_name, credential_password))
                        print('\n')
                        print(
                            f"Credentials for *{ credential_name }* has been created and saved successfully")
                        print('\n')

        elif short_code == 'gp':
            print(" ")
            print("     ***TO GENERATE A PASSWORD, ENTER YOUR NAME AND ACCOUNT BELOW")
            print(" ")
            list_of_inputs = [c for c in input()]
            list_of_inputs.reverse()
            print(list_of_inputs)

        elif short_code == "ex":
            print("-"*130)
            print(" ")
            print("         BYE CHOOMBA...")
            print(" ")
            print("-"*130)
            break


if __name__ == '__main__':

    password_app()

