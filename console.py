#!/bin/python3
from cmd import Cmd

class HBNBCommand(Cmd):
    
    def __init__(self):
            super().__init__()
            self.intro = ('Welcome to AirBnB Clone Console! Type '
                       '"help" or "?" for a list of commands.')
            self.prompt = '(hbnb) '

    @staticmethod
    def do_exit(self):
        """Exit the program."""
        return True


    @staticmethod
    def do_EOF(self):
        """EOF signal (usually ctl+d) will run this to exit the program."""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
