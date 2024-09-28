#!/bin/python3
"""
module documentation WIP.
This is the main module for running the command line interpreter,
aka the console. Run this to run the command line interpreter.
"""
import sys
import webbrowser
from cmd import Cmd
from os import isatty
from time import sleep

from models.colors import *


class HBNBCommand(Cmd):
    """
    the main command line interpreter class
    """
    def __init__(self):
        super().__init__()
        if isatty(sys.stdin.isatty()):  # only sets intro in interactive
            self.intro = ('Welcome to AirBnB Clone Console! Type '
                          '"help" or "?" for a list of commands. Type '
                          '"exit" or "quit" to exit.')
            self.prompt = '(hbnb) \033[7m'  # reverses background & foreground
        else:
            self.prompt = '(hbnb) '

    def precmd(self, line):
        """
        overrides the default method the runs between when the input is parsed
        and when the command is run. This override resets the text color to
        undo the effect from adding \033[7m to the prompt, which reverses the
        background and foreground colors for the user input. This makes sure
        that the output doesn't retain this effect.
        :param line: user input
        :return: the same thing the original command returns, which is line,
        according to the source code for cmd.py.
        """
        reset_color()
        return super().precmd(line)

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

    @staticmethod
    def do_selfdestruct(timer: str):
        """
Activates self-destruct mode. If there is no number given, it will count down
from 5.
Arguments: number (optional) - amount of seconds to count down from
Usage: selfdestruct <number>
        """
        t = 5
        if timer.isnumeric():
            t = int(timer)
        elif timer != '':
            print("Please specify a valid number, or leave blank.")
            return

        set_color('red')
        set_color('bold')
        set_color('reverse')
        set_color('blinking')
        print("SELF DESTRUCT MODE INITIATED.\n")
        reset_color()
        while t > 0:
            if t <= 3:
                set_color('light red')
            else:
                reset_color()
            sleep(1)
            print(t)
            t -= 1
        sleep(1)
        reset_color()
        set_color('yellow')
        # set_color('reverse')
        print("Console has been obliterated. Goodbye.")
        reset_color()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
