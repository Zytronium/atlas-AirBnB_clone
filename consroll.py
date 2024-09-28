#!/bin/python3
"""
module documentation WIP.
This is a secondary module, which runs the command line interpreter,
aka the console. However, running this will give you a special surprise!
Every time you run a command. Any command. Even EOF.
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
            self.intro = ('Welcome to AirBnB Clone Consroll! Type '
                          '"help" or "?" for a list of commands. Type '
                          '"exit" or "quit" for a surprise.')
            self.prompt = '(rckrlBnB) \033[7m'  # reverses background & foreground
        else:
            self.prompt = '(rckrlBnB) '

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
        print("Never gonna give you up!")

    def default(self, line):
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    @staticmethod
    def do_rickroll(self):
        """Rickrolls you"""
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
