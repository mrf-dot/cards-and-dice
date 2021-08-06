"""Main file"""
from termcolor import cprint
from getpass import getuser
import commands


def changeName():
    commands.clear()
    changeName = input('What would you like me to call you?: ')
    commands.name = changeName if changeName else getuser()
    commands.clear()


def main():
    """Initiates the program

    """
    changeName()
    commands.help()
    while True:
        selection = input('Select an option: ').lower()
        default = lambda: cprint(f'\"{selection}\" is not a valid command.',
                                 'red')
        getattr(commands, selection, lambda: default())()


if __name__ == '__main__':
    main()