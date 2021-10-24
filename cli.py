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
