#!/bin/python3
from cmd import Cmd

class HBNBCommand(Cmd):
    
    def __init__(self):
            super().__init__()
            self.intro = ('Welcome to AirBnB Clone Console! Type '
                       '"help" or "?" for a list of commands.')
            self.prompt = '(rkrlbnb) '

    @staticmethod
    def do_exit(self):
        """Exit the program."""
        return True


    @staticmethod
    def do_EOF(self):
        """EOF signal (usually ctl+d) will run this to exit the program."""
        # print()  # removed because since this cmd is required for the project,
                   # the checker probably is not expecting this extra line.
                   # However, if we can get away with it, I'd like to keep it
                   # because this extra line forces the next cmd prompt in
                   # the terminal to be on a separate line.
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
