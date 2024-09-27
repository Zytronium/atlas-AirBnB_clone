#!/bin/python3
"""
module documentation WIP.
This is the main module for running the command line interface,
aka the console. Run this to run the command line interface.
"""
import sys
import webbrowser
from cmd import Cmd
from os import isatty


class HBNBCommand(Cmd):
    """
    the main command line interface class
    """
    def __init__(self):
        super().__init__()
        if isatty(sys.stdin.isatty()):  # only sets intro in interactive
            self.intro = ('Welcome to AirBnB Clone Console! Type '
                          '"help" or "?" for a list of commands. Type '
                          '"exit" or "quit" to exit.')
        self.prompt = '(hbnb) '

    def emptyline(self):
        """
        overrides default method that runs when en empty command is run.
        Instead, it will do nothing when there is no command.
        """
        pass

    # ======================== user commands ========================
    @staticmethod
    def do_exit(self):
        """Exit the program."""
        return True

    @staticmethod
    def do_quit(self):
        """Exit the program."""
        return True

    @staticmethod
    def do_EOF(self):
        """EOF signal (usually ctl+d) will run this to exit the program."""
        print()  # Prints an extra line to force the next cmd prompt in
                 # the terminal to be on a separate line.
        return True

    @staticmethod
    def do_rickroll(self):
        """Rickrolls you"""
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
